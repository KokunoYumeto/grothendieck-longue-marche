# Exact first-crop coordinate recovery by pixel reproduction

Verified 2026-11-21 15:24:47 UTC using Pillow 13.0.0.

## Result

All five requested rectangles are recovered and verified against every RGB channel value of their existing saved crops. The acceptance criterion is zero differing channel values and identical full RGB pixel hashes. Template correlation alone was not accepted as coordinate provenance.

| Saved crop | Original rectangle (x0, y0, x1, y1) | Saved pixels | Sharpening | Differing channel values |
|---|---|---|---|---|
| crops/149_scan005_c19.png | (465, 865, 1130, 1005) | 2600 × 547 | UnsharpMask 1.5 / 120 / 3 | 0 |
| crops/149_scan010_c14.png | (1172, 2080, 1631, 2189) | 2600 × 617 | UnsharpMask 1.5 / 120 / 3 | 0 |
| crops/149_scan010_c15.png | (272, 2184, 741, 2289) | 2600 × 582 | UnsharpMask 1.5 / 120 / 3 | 0 |
| crops/149_scan010_c16.png | (925, 2242, 1265, 2345) | 2600 × 788 | UnsharpMask 1.5 / 120 / 3 | 0 |
| crops/149_scan018_c10.png | (280, 1411, 624, 1525) | 2600 × 862 | None | 0 |

Coordinates use the original JPEG pixel grid. Left/top are inclusive; right/bottom are exclusive, as in Pillow `Image.crop`.

## Discovery and verification

The existing metadata supplied a candidate for scan018 c10. Applying autocontrast with cutoff 0.5 before the resize reproduced that saved crop exactly. The earlier test without this contrast step had failed.

For the other four, a pixel-only scale search compared each saved crop with its original scan using FFT normalized cross-correlation. Both were downsampled by about three for initial location/scale discovery. The search was then refined on the original pixel grid, considering integer rectangle widths/heights whose rounded 2600-pixel-wide output matched the saved dimensions. No handwriting was read, no OCR was performed, and no proposed source text was used as a template.

The best integer rectangles initially reproduced almost all pixels with autocontrast 0.5 and LANCZOS, but sparse edge differences remained. A parameter search on an interior pixel tile identified UnsharpMask radius 1.5, percent 120, threshold 3. That candidate filter was then applied to each entire reproduced image. All four complete RGB arrays became identical to their saved targets. The tile search was only a way to discover parameters; acceptance required the complete-image checks.

The established reproducing pipeline is:

1. Open the original JPEG and convert to RGB.
2. Crop the exact integer rectangle in the table.
3. Apply `ImageOps.autocontrast(..., cutoff=0.5)`.
4. Resize to `(2600, round(height*2600/width))` with LANCZOS.
5. For scan005 c19 and scan010 c14/c15/c16 only, apply `ImageFilter.UnsharpMask(radius=1.5, percent=120, threshold=3)`.
6. Compare every output RGB channel value with the existing PNG.

No rotation, resampling of the source scan beforehand, additional contrast enhancement, or source-image edit is needed. This records an exactly reproducing pipeline; it does not claim that the historical shell command itself was recovered or that all conceivable processing pipelines are unique.

## Reproduction

Run from the workspace root:

```sh
python3 edition/documentation/recover_first_crop_pixels.py
```

The default invocation is read-only. It checks output dimensions, the `ImageChops` difference bounding box, the count of nonzero values in each difference channel, the maximum channel difference, and full RGB pixel hashes. It fails immediately if any target differs. `--record` is the explicit one-time evidence/coordinate-table write mode.

## Hash evidence

Verification-script SHA-256: `2d19ca48d86c4fb0841b6a73039e86eb8dbc57151fc55b965c23c2949c6ba109`.

The machine-readable companion `coordinate_recovery_reader_c.json` records source-file, saved-PNG-file, saved-RGB-pixel, and reproduced-RGB-pixel SHA-256 hashes, dimensions, parameters, and zero-difference counts for all five cases.

### crops/149_scan005_c19.png

- Source SHA-256: `b95c557ab9ec40378cbbe1745ca2698065d1d3feb5e753d6d26882afaeea16ac`
- Saved PNG SHA-256: `0493484b8e29a5d1e67b4c3e645a0d1bae5ff6b47e577167602ab73b51f4ff2f`
- Saved and reproduced RGB SHA-256: `d10baf16a3e4e3666c7937fc488c06e2cae9992a9c1c33fc3ce28f36cbeedc76`
- RGB channel values compared: 4,266,600; differing values: 0; maximum difference: 0.

### crops/149_scan010_c14.png

- Source SHA-256: `0ce5404efee21dc0140bf389a34263657092b25c45c6f0db6cc97ba9aaca9b17`
- Saved PNG SHA-256: `dfad42769f560bcf5b5990c528e2a867f71c0be387cf72b2c5f55057d86fef1f`
- Saved and reproduced RGB SHA-256: `51501c3dcad69da941cf87d845272ff60700da0dcd183b3d5b5e48264b08102a`
- RGB channel values compared: 4,812,600; differing values: 0; maximum difference: 0.

### crops/149_scan010_c15.png

- Source SHA-256: `0ce5404efee21dc0140bf389a34263657092b25c45c6f0db6cc97ba9aaca9b17`
- Saved PNG SHA-256: `1ed905e92b46e5662211b010e126ec77f785b527a41a9b24f1538b602eb7d2cc`
- Saved and reproduced RGB SHA-256: `36eea6badc60739a4f2fef20f887229ffee85020f0685458152be9e15fb83dd4`
- RGB channel values compared: 4,539,600; differing values: 0; maximum difference: 0.

### crops/149_scan010_c16.png

- Source SHA-256: `0ce5404efee21dc0140bf389a34263657092b25c45c6f0db6cc97ba9aaca9b17`
- Saved PNG SHA-256: `6388737b8f238a0ef696ee277a53130cd63d8e3233be91a522a82b5fedf115bc`
- Saved and reproduced RGB SHA-256: `86af792b49861398afe13bf987186cf303dc32d49a5240d29944dba84e121bd0`
- RGB channel values compared: 6,146,400; differing values: 0; maximum difference: 0.

### crops/149_scan018_c10.png

- Source SHA-256: `98498989188eeeef8579491448d5eaad2bf39b991848e7ebae0f5db602528108`
- Saved PNG SHA-256: `fe0148639597f5a51512ef48e2514c57a8615273a18ae001218dcba51d6775ff`
- Saved and reproduced RGB SHA-256: `9b4196bade6d97c665e1d8284d5968b4b6b9215dccb92c43f65265a917cdbade`
- RGB channel values compared: 6,723,600; differing values: 0; maximum difference: 0.

## Mutation scope

Only the five proven rows are appended to `first_crop_coordinates.tsv`. The existing rows are preserved byte-for-byte. This evidence note, its JSON companion, and the verification script are separate new documentation. No original scan, saved crop, page, review JSON, frozen TSV, or adjudication file was modified.
