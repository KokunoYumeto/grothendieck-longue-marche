"""Recover a note's text from an Obsidian file-recovery snapshot (an IndexedDB blob file), read-only.

Usage: python -I recover_obsidian_snapshot.py <blob file> <expected note path> <output file>
The blob holds a V8-serialized object {path, ts, data}. Prints the path, the snapshot time (UTC), the length and the
line count, and writes the data as UTF-8 (LF line ends as stored). Nothing in the Obsidian store is changed.
"""
import datetime
import struct
import sys

sys.stdout.reconfigure(encoding="utf-8")
blob, expected, out = sys.argv[1], sys.argv[2], sys.argv[3]
b = open(blob, "rb").read()


def varint(pos):
    n = shift = 0
    while True:
        c = b[pos]
        pos += 1
        n |= (c & 0x7F) << shift
        shift += 7
        if not c & 0x80:
            return n, pos


def read_string(pos):
    while b[pos] == 0x00:  # padding before two-byte strings
        pos += 1
    tag = b[pos]
    n, p = varint(pos + 1)
    if tag == 0x63:  # 'c': two-byte (UTF-16LE)
        return b[p:p + n].decode("utf-16-le"), p + n
    if tag == 0x22:  # '"': one-byte (Latin-1)
        return b[p:p + n].decode("latin-1"), p + n
    if tag == 0x53:  # 'S': UTF-8
        return b[p:p + n].decode("utf-8"), p + n
    raise SystemExit("unexpected string tag %#x at %d" % (tag, pos))


start = b.find(b"\xff\x0f\x6f")  # V8 version 15, begin object
assert start >= 0, "no V8 object header"
pos, fields = start + 3, {}
while len(fields) < 3:
    key, pos = read_string(pos)
    if key == "ts":
        assert b[pos] == 0x4E, "ts is not a double"
        fields["ts"] = struct.unpack("<d", b[pos + 1:pos + 9])[0]
        pos += 9
    else:
        fields[key], pos = read_string(pos)
assert fields["path"] == expected, fields["path"]
ts = datetime.datetime.fromtimestamp(fields["ts"] / 1000, datetime.timezone.utc)
text = fields["data"]
open(out, "w", encoding="utf-8", newline="").write(text)
print("path:", fields["path"])
print("snapshot time (UTC):", ts.strftime("%Y-%m-%d %H:%M:%S"))
print("characters:", len(text), " lines (LF):", text.count("\n"), " splitlines:", len(text.splitlines()))
print("written:", out)
