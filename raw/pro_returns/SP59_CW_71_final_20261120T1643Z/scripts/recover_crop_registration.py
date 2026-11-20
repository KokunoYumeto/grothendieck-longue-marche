#!/usr/bin/env python3
"""Numerical crop provenance recovery; no OCR, semantic readings, or image output.

SIFT descriptors and RANSAC estimate the saved-crop to original-page transform.
Only tabular numerical metadata and a Markdown report are saved. The source and
existing crop are never modified. OpenCV, NumPy, SciPy, and Pillow are required.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import math
import sys
from pathlib import Path

import numpy as np
from PIL import Image


def write_tsv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("crop", type=Path)
    parser.add_argument("--prefix", type=Path, required=True)
    parser.add_argument("--dependency-path", type=Path)
    parser.add_argument("--crop-widths", type=int, nargs="+", default=[600, 900, 1200])
    parser.add_argument("--ratios", type=float, nargs="+", default=[0.70, 0.78, 0.85])
    parser.add_argument("--ransac-threshold", type=float, default=2.0)
    args = parser.parse_args()
    dependencies = args.dependency_path or Path(__file__).resolve().parents[2] / "support/registration_dependencies"
    if dependencies.exists():
        sys.path.insert(0, str(dependencies))
    import cv2

    cv2.setNumThreads(2)
    cv2.setRNGSeed(617008)
    source = Image.open(args.source)
    crop = Image.open(args.crop)
    source_gray = np.asarray(source.convert("L"))
    full_width, full_height = crop.size
    detector = cv2.SIFT_create(nfeatures=25000, contrastThreshold=0.015, edgeThreshold=20)
    source_points, source_descriptors = detector.detectAndCompute(source_gray, None)
    print(f"SIFT source keypoints: {len(source_points)}", flush=True)
    matcher = cv2.BFMatcher(cv2.NORM_L2)
    trials = []
    correspondence_rows = []
    for width in args.crop_widths:
        height = round(full_height * width / full_width)
        reduced = crop.convert("L").resize((width, height), Image.Resampling.LANCZOS)
        points, descriptors = detector.detectAndCompute(np.asarray(reduced), None)
        if descriptors is None:
            continue
        matches = matcher.knnMatch(descriptors, source_descriptors, k=2)
        for ratio in args.ratios:
            accepted = [pair[0] for pair in matches if len(pair) == 2 and pair[0].distance < ratio * pair[1].distance]
            # A source descriptor contributes only one correspondence.
            unique = {}
            for match in sorted(accepted, key=lambda x: x.distance):
                unique.setdefault(match.trainIdx, match)
            accepted = list(unique.values())
            if len(accepted) < 3:
                print(f"width={width}, ratio={ratio}: insufficient matches ({len(accepted)})", flush=True)
                continue
            target_xy = np.asarray([points[m.queryIdx].pt for m in accepted], dtype=np.float64)
            target_xy = (target_xy + 0.5) * np.asarray([full_width / width, full_height / height]) - 0.5
            source_xy = np.asarray([source_points[m.trainIdx].pt for m in accepted], dtype=np.float64)
            for model in ["similarity", "affine"]:
                if model == "similarity":
                    transform, mask = cv2.estimateAffinePartial2D(target_xy, source_xy,
                        method=cv2.RANSAC, ransacReprojThreshold=args.ransac_threshold,
                        maxIters=30000, confidence=0.9999, refineIters=30)
                else:
                    transform, mask = cv2.estimateAffine2D(target_xy, source_xy,
                        method=cv2.RANSAC, ransacReprojThreshold=args.ransac_threshold,
                        maxIters=30000, confidence=0.9999, refineIters=30)
                if transform is None:
                    continue
                inlier = mask.ravel().astype(bool)
                predictions = target_xy @ transform[:, :2].T + transform[:, 2]
                residual = np.linalg.norm(predictions - source_xy, axis=1)
                matrix = transform[:, :2]
                center = matrix @ np.asarray([(full_width - 1) / 2, (full_height - 1) / 2]) + transform[:, 2]
                scale_x = np.linalg.norm(matrix[:, 0])
                scale_y = np.linalg.norm(matrix[:, 1])
                angle = math.degrees(math.atan2(matrix[1, 0], matrix[0, 0]))
                trial_id = f"w{width}_r{ratio:.2f}_{model}"
                row = dict(trial=trial_id, model=model, reduced_width=width, reduced_height=height,
                    ratio=ratio, source_keypoints=len(source_points), crop_keypoints=len(points),
                    matches=len(accepted), inliers=int(inlier.sum()),
                    inlier_rmse=float(np.sqrt(np.mean(residual[inlier] ** 2))),
                    inlier_max_error=float(residual[inlier].max()),
                    inlier_span_x=float(np.ptp(target_xy[inlier, 0])),
                    inlier_span_y=float(np.ptp(target_xy[inlier, 1])),
                    a00=matrix[0,0], a01=matrix[0,1], a10=matrix[1,0], a11=matrix[1,1],
                    tx=transform[0,2], ty=transform[1,2],
                    determinant=float(np.linalg.det(matrix)), angle_degrees=angle,
                    source_center_x=center[0], source_center_y=center[1],
                    expanded_width_estimate=full_width * scale_x,
                    expanded_height_estimate=full_height * scale_y,
                    normalized_column_dot=float(np.dot(matrix[:,0],matrix[:,1])/(scale_x*scale_y)))
                trials.append(row)
                for i, match in enumerate(accepted):
                    correspondence_rows.append(dict(trial=trial_id, crop_x=target_xy[i,0],crop_y=target_xy[i,1],
                        source_x=source_xy[i,0],source_y=source_xy[i,1],descriptor_distance=match.distance,
                        inlier=int(inlier[i]),reprojection_error=residual[i]))
                print(f"{trial_id}: {inlier.sum()}/{len(accepted)} inliers; RMSE {row['inlier_rmse']:.5f}; "
                    f"angle {angle:.5f}; center {center}; native expansion {row['expanded_width_estimate']:.3f} x {row['expanded_height_estimate']:.3f}", flush=True)

    if not trials:
        raise SystemExit("No registration model obtained; no coordinates accepted.")
    trials.sort(key=lambda r: (-r["inliers"], r["inlier_rmse"]))
    write_tsv(args.prefix.with_name(args.prefix.name + "_transforms.tsv"), trials, list(trials[0]))
    write_tsv(args.prefix.with_name(args.prefix.name + "_correspondences.tsv"), correspondence_rows, list(correspondence_rows[0]))
    report = ["# Numerical crop registration", "",
        "This is image geometry metadata only. No OCR, semantic reading, image display, or image output was performed.", "",
        f"- Source: `{args.source}`; SHA-256 `{file_hash(args.source)}`; size {source.width} × {source.height}.",
        f"- Existing crop: `{args.crop}`; SHA-256 `{file_hash(args.crop)}`; size {full_width} × {full_height}.",
        f"- OpenCV version: {cv2.__version__}; SIFT descriptors, nearest-neighbour ratio matching, and RANSAC similarity/full-affine models.",
        f"- Source descriptors: {len(source_points)}; retained models: {len(trials)}.",
        "- Registration parameters are estimates. Exact source coordinates are not accepted without a successful pipeline verification.", "",
        "## Ranked numerical models", "",
        "| Trial | Inliers | Source-pixel RMSE | Angle | Source center | Expanded native dimensions |",
        "|---|---:|---:|---:|---|---|"]
    for row in trials:
        report.append(f"| {row['trial']} | {row['inliers']} | {row['inlier_rmse']:.6f} | {row['angle_degrees']:.6f} | "
            f"({row['source_center_x']:.6f}, {row['source_center_y']:.6f}) | "
            f"{row['expanded_width_estimate']:.6f} × {row['expanded_height_estimate']:.6f} |")
    args.prefix.with_suffix(".md").write_text("\n".join(report) + "\n")


if __name__ == "__main__":
    main()
