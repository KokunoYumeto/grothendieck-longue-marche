# Exact crop-pipeline verification

Numerical image geometry only: no OCR, semantic reading, display, saved image, or transcription change.

- Source SHA-256: `4b56f6736ada508943f8379c0a74365d5e5ff9eed14b8c4f7b08326ee8c501ba`.
- Existing crop SHA-256: `20147642b901c8f08f8981f39469d965a2cdbebf06378bc1e77469a42f0f7b98`.
- Registration: `output/metadata/crop008_feature_registration`; 18 models passed the stated 50-inlier gate.
- Median estimated angle -34.022848546; center (1109.679708664, 1052.199924412); expanded dimensions (332.375900251, 317.307846724).
- Replayed angles: [-34.0]; integer size radius ±12; origin radius ±2; expanded-dimension tolerance ±2.0.
- Exact-dimension candidates tested: 200; byte-identical results: 1; distinct exact boxes: 1.
- Replay exactly follows crop.py: integer source box; nearest-neighbour rotate with expansion and white fill; autocontrast; width-2400 LANCZOS resize; UnsharpMask(1.5,130,3); JPEG quality95.

## Exact reproductions

| Box | Rotation parameter | JPEG SHA-256 | Decoded pixel RMSE |
|---|---:|---|---:|
| (980,950,1240,1155) | -34.0 | `20147642b901c8f08f8981f39469d965a2cdbebf06378bc1e77469a42f0f7b98` | 0.0 |

## Interpretation

Byte equality proves this source box and rotation reproduce the saved crop under the documented pipeline. It does not recover the original shell command. Nearest-neighbour rotation can make a tiny interval of angles produce the same pixels; the reported angle is an exactly reproducing parameter, not proof of the original command's floating-point spelling.
