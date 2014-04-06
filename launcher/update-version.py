#!/usr/bin/env python
import os
import sys


def update_version(path, strict=False, update_series=False):
    if not os.path.exists(path):
        print(path, "does not exist, not updating version")
        return
    print("updating version number in", path)

    ver = version
    with open(path, "rb") as f:
        data = f.read()

    data = data.replace("9.8.7dummy3", version_3)
    data = data.replace("9.8.7dummy", version)
    data = data.replace("9.8.7", version_3 if strict else version)
    if update_series:
        data = data.replace("unknown", series)
    with open(path, "wb") as f:
        f.write(data)


with open("VERSION", "rb") as f:
    version = f.read().strip()

parts = version.split(".")
parts = parts[:3]
for i, part in enumerate(parts):
    p = ""
    for c in part:
        if c in "0123456789":
            p += c
        else:
            break
    parts[i] = p
version_3 = ".".join(parts)

with open("SERIES", "rb") as f:
    series = f.read().strip()

update_version(
    sys.argv[1], update_series=("--update-series" in sys.argv),
    strict=("--strict" in sys.argv))
