import sys
import os

args = sys.argv[1:]

flag_a = False
directory = "."

for arg in args:
    if arg == "-a":
        flag_a = True
    elif arg == "-1":
        continue
    else:
        directory = arg

entries = sorted(os.listdir(directory))

for entry in entries:
    if not flag_a and entry.startswith("."):
        continue
    print(entry)