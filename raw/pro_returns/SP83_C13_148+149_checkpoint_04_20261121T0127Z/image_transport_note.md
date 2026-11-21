# Image display transport

The canonical cropped images are the PNG files in `crops/`. Some were too large for the image tool’s response limit. Those PNG files were preserved unchanged. Display transport used a lossless WebP made from the PNG at identical dimensions, with decoded RGB pixel equality verified by `scripts/lossless_transport.py`.

For the following four oversized crops, even the lossless transport exceeded the response limit. The reader and main reader displayed a JPEG at quality 98, chroma subsampling disabled, and the same dimensions as the canonical PNG. This compression is lossy; it changed neither the crop boundary nor its resolution. The canonical PNG, not the transport JPEG, is retained for review.

- `148_scan067_pants.png` → `148_scan067_pants_q98.jpg`
- `148_scan067_pencil_map.png` → `148_scan067_pencil_map_q98.jpg`
- `148_scan067_pencil_map_full.png` → `148_scan067_pencil_map_full_q98.jpg`
- `148_scan067_triangle1_full.png` → `148_scan067_triangle1_full_q98.jpg`

A failed or truncated image-tool response was not counted as a reading. Successful image displays were logged in `records/main_review_crops.json`. Re-display after transport failure did not create another cropped place.
