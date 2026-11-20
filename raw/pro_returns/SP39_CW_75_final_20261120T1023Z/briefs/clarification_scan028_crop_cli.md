# Common implementation clarification during scan 028

Sent to all three readers after A reported that --help was unsupported:

`crop.py SOURCE OUTPUT MANIFEST X0 Y0 X1 Y1 [WIDTH=2800] [ROTATE=0]`

Coordinates are full-image pixels. The helper applies autocontrast, LANCZOS enlargement and UnsharpMask and records the exact bounds. Reading this prescribed helper implementation is allowed. It is workflow documentation, not another manuscript source. No image was reopened for this clarification.
