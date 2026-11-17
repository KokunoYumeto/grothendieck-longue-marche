# Lossless image-container compression from checkpoint27

The read-only checkpoint26 measurement compressed the identical prior
440780800-byte image TAR with the standard ZIP_LZMA codec and measured
364203729 compressed bytes against414952165 with DEFLATE, a saving of
50748436bytes. It created no ZIP and altered no archive. Its complete
producer, actual output and measurement JSON remain retained.

We now select ZIP_LZMA for the image TAR only when the checkpoint number
is at least27. Historical documents and text already use standard ZIP_LZMA.
The TAR construction, original path/byte manifests, standard hardlinks,
current direct main PDF and independent restoration procedures are unchanged.
Every prior archive, including the captured/saved26, remains byte-exactly
unchanged. The complete pre-change packager source is retained separately.

This is a storage encoding change, not removal or replacement of any
mathematical content or image bytes. The next actual archive still requires
its own conservative size estimate, CRC and every-entry/version verification,
plus independent native restoration of both TAR containers. The measured
compression took about406seconds, so the hourly capture may take longer;
its review remains scheduled for03:49:30UTC. No extra ZIP is created for
this change or for testing it.
