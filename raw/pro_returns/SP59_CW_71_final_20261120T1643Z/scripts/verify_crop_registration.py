#!/usr/bin/env python3
"""Verify numerical crop-registration candidates by exact in-memory pipeline replay.

Writes TSV/Markdown numerical provenance only. Never writes or displays an image.
The source, existing crop, transcription, and authoritative crop registers are
read-only. Geometric candidates remain provisional unless exact replay succeeds.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter, ImageOps


def read_tsv(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def write_tsv(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def geometry(w, h, degrees):
    angle = degrees % 360.0
    a = -math.radians(angle)
    rotation = np.array([[round(math.cos(a), 15), round(math.sin(a), 15)],
                         [round(-math.sin(a), 15), round(math.cos(a), 15)]])
    if angle in (0.0, 180.0):
        width, height = w, h
    elif angle in (90.0, 270.0):
        width, height = h, w
    else:
        center = np.array([w / 2, h / 2])
        offset = center - rotation @ center
        corners = np.array([(0,0), (w,0), (w,h), (0,h)], dtype=float) @ rotation.T + offset
        width = math.ceil(corners[:,0].max()) - math.floor(corners[:,0].min())
        height = math.ceil(corners[:,1].max()) - math.floor(corners[:,1].min())
    offset = np.array([w / 2, h / 2]) - rotation @ np.array([width / 2, height / 2])
    return width, height, rotation, offset


def native_pipeline(source, box, angle):
    result = source.crop(box)
    if angle:
        result = result.rotate(angle, expand=True, fillcolor="white")
    return ImageOps.autocontrast(result)


def saved_pipeline(source, box, angle):
    result = native_pipeline(source, box, angle)
    result = result.resize((2400, round(result.height * 2400 / result.width)), Image.Resampling.LANCZOS)
    result = result.filter(ImageFilter.UnsharpMask(radius=1.5, percent=130, threshold=3))
    stream = io.BytesIO()
    result.save(stream, format="JPEG", quality=95)
    return stream.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("crop", type=Path)
    parser.add_argument("--registration-prefix", type=Path, required=True)
    parser.add_argument("--prefix", type=Path, required=True)
    parser.add_argument("--angles", type=float, nargs="+")
    parser.add_argument("--size-radius", type=int, default=12)
    parser.add_argument("--origin-radius", type=int, default=2)
    parser.add_argument("--expansion-tolerance", type=float, default=2.0)
    args = parser.parse_args()
    transforms = read_tsv(args.registration_prefix.with_name(args.registration_prefix.name + "_transforms.tsv"))
    correspondences = read_tsv(args.registration_prefix.with_name(args.registration_prefix.name + "_correspondences.tsv"))
    reliable = [r for r in transforms if int(r["inliers"]) >= 50 and float(r["determinant"]) > 0]
    if not reliable:
        raise SystemExit("No transform meets the stated 50-inlier positive-determinant gate.")
    center_x = float(np.median([float(r["source_center_x"]) for r in reliable]))
    center_y = float(np.median([float(r["source_center_y"]) for r in reliable]))
    angle_est = float(np.median([float(r["angle_degrees"]) for r in reliable]))
    width_est = float(np.median([float(r["expanded_width_estimate"]) for r in reliable]))
    height_est = float(np.median([float(r["expanded_height_estimate"]) for r in reliable]))
    angles = args.angles or [float(round(angle_est))]
    best = min(reliable, key=lambda r: float(r["inlier_rmse"]))
    pairs = [r for r in correspondences if r["trial"] == best["trial"] and r["inlier"] == "1"]
    q = np.array([[float(r["crop_x"]), float(r["crop_y"])] for r in pairs])
    p = np.array([[float(r["source_x"]), float(r["source_y"])] for r in pairs])
    source = Image.open(args.source)
    crop = Image.open(args.crop)
    target_bytes = args.crop.read_bytes()
    target_hash = hashlib.sha256(target_bytes).hexdigest()
    target_array = np.asarray(crop).astype(np.int16)
    preview_size = (240, round(crop.height * 240 / crop.width))
    target_preview = np.asarray(crop.convert("L").resize(preview_size, Image.Resampling.LANCZOS), dtype=np.float32)
    rows = []
    for angle in angles:
        c, s = abs(math.cos(math.radians(angle))), abs(math.sin(math.radians(angle)))
        denominator = c*c - s*s
        if abs(denominator) < 0.1:
            raise SystemExit("Near-45-degree inverse size geometry requires a broader explicit search; stopped.")
        estimated_w = (c * width_est - s * height_est) / denominator
        estimated_h = (c * height_est - s * width_est) / denominator
        for w in range(max(2, round(estimated_w)-args.size_radius), round(estimated_w)+args.size_radius+1):
            for h in range(max(2, round(estimated_h)-args.size_radius), round(estimated_h)+args.size_radius+1):
                width, height, rotation, offset = geometry(w,h,angle)
                if abs(width-width_est) > args.expansion_tolerance or abs(height-height_est) > args.expansion_tolerance:
                    continue
                if round(height * 2400 / width) != crop.height:
                    continue
                matrix = rotation @ np.diag([width/crop.width, height/crop.height])
                origin_x = round(center_x - (w-1)/2)
                origin_y = round(center_y - (h-1)/2)
                for x0 in range(origin_x-args.origin_radius, origin_x+args.origin_radius+1):
                    for y0 in range(origin_y-args.origin_radius, origin_y+args.origin_radius+1):
                        box = (x0,y0,x0+w,y0+h)
                        if not (0<=x0<box[2]<=source.width and 0<=y0<box[3]<=source.height):
                            continue
                        translation = np.array([x0,y0])+offset+matrix@np.array([0.5,0.5])-np.array([0.5,0.5])
                        residual = q@matrix.T+translation-p
                        reprojection = float(np.sqrt(np.mean(np.sum(residual**2,axis=1))))
                        preview = native_pipeline(source,box,angle).convert("L").resize(preview_size,Image.Resampling.LANCZOS)
                        preview_mse = float(np.mean((np.asarray(preview,dtype=np.float32)-target_preview)**2))
                        rows.append(dict(x0=x0,y0=y0,x1=x0+w,y1=y0+h,width=w,height=h,
                            angle=angle,expanded_width=width,expanded_height=height,
                            feature_reprojection_rmse=reprojection,preview_mse=preview_mse,
                            exact_jpeg_match="not checked",decoded_pixels_match="not checked",
                            decoded_pixel_rmse="",candidate_jpeg_sha256=""))
    rows.sort(key=lambda row: (row["preview_mse"],row["feature_reprojection_rmse"]))
    print(f"Geometry candidates: {len(rows)}; all will receive exact byte replay.",flush=True)
    if not rows:
        raise SystemExit("No exact output-dimension candidates; no coordinates accepted.")
    for index,row in enumerate(rows):
        data=saved_pipeline(source,(row["x0"],row["y0"],row["x1"],row["y1"]),row["angle"])
        digest=hashlib.sha256(data).hexdigest()
        row["candidate_jpeg_sha256"]=digest
        row["exact_jpeg_match"]="yes" if digest==target_hash else "no"
        if index<20 or digest==target_hash:
            array=np.asarray(Image.open(io.BytesIO(data))).astype(np.int16)
            row["decoded_pixels_match"]="yes" if np.array_equal(array,target_array) else "no"
            difference=array.astype(np.float64)-target_array
            row["decoded_pixel_rmse"]=float(np.sqrt(np.mean(difference*difference)))
        if digest==target_hash:
            print(f"EXACT JPEG REPLAY: box={(row['x0'],row['y0'],row['x1'],row['y1'])}, angle={row['angle']}, sha256={digest}",flush=True)
        if (index+1)%20==0 or index==len(rows)-1:
            print(f"Replayed {index+1}/{len(rows)}",flush=True)
    write_tsv(args.prefix.with_suffix(".tsv"),rows)
    exact=[r for r in rows if r["exact_jpeg_match"]=="yes"]
    boxes=sorted(set((r["x0"],r["y0"],r["x1"],r["y1"]) for r in exact))
    report=["# Exact crop-pipeline verification","",
        "Numerical image geometry only: no OCR, semantic reading, display, saved image, or transcription change.","",
        f"- Source SHA-256: `{hashlib.sha256(args.source.read_bytes()).hexdigest()}`.",
        f"- Existing crop SHA-256: `{target_hash}`.",
        f"- Registration: `{args.registration_prefix}`; {len(reliable)} models passed the stated 50-inlier gate.",
        f"- Median estimated angle {angle_est:.9f}; center ({center_x:.9f}, {center_y:.9f}); expanded dimensions ({width_est:.9f}, {height_est:.9f}).",
        f"- Replayed angles: {angles}; integer size radius ±{args.size_radius}; origin radius ±{args.origin_radius}; expanded-dimension tolerance ±{args.expansion_tolerance}.",
        f"- Exact-dimension candidates tested: {len(rows)}; byte-identical results: {len(exact)}; distinct exact boxes: {len(boxes)}.",
        "- Replay exactly follows crop.py: integer source box; nearest-neighbour rotate with expansion and white fill; autocontrast; width-2400 LANCZOS resize; UnsharpMask(1.5,130,3); JPEG quality95.","",
        "## Exact reproductions","","| Box | Rotation parameter | JPEG SHA-256 | Decoded pixel RMSE |","|---|---:|---|---:|"]
    for row in exact:
        report.append(f"| ({row['x0']},{row['y0']},{row['x1']},{row['y1']}) | {row['angle']} | `{row['candidate_jpeg_sha256']}` | {row['decoded_pixel_rmse']} |")
    if not exact:
        report.append("| None | — | — | — |")
    report.extend(["","## Interpretation","",
        "Byte equality proves this source box and rotation reproduce the saved crop under the documented pipeline. It does not recover the original shell command. Nearest-neighbour rotation can make a tiny interval of angles produce the same pixels; the reported angle is an exactly reproducing parameter, not proof of the original command's floating-point spelling." if len(boxes)==1 else
        "A unique exactly reproducing box was not established. Retain the unknown coordinate status; registration estimates and ranked candidates alone are not accepted coordinates."])
    args.prefix.with_suffix(".md").write_text("\n".join(report)+"\n")


if __name__=="__main__":
    main()
