import sys, os, zipfile
zpath, dest = sys.argv[1], sys.argv[2]
if os.path.exists(dest) and os.listdir(dest):
    sys.exit("destination not empty")
os.makedirs(dest, exist_ok=True)
destabs = os.path.realpath(dest)
with zipfile.ZipFile(zpath) as z:
    names = z.namelist()
    for n in names:
        target = os.path.realpath(os.path.join(destabs, n))
        if not (target == destabs or target.startswith(destabs + os.sep)):
            sys.exit("unsafe path in zip: " + n)
    z.extractall(destabs)
    tot = sum(i.file_size for i in z.infolist())
print(len(names), "entries,", tot, "bytes")
