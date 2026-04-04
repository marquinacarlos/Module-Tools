import sys
import os

args = sys.argv[1:]

flag_l = False
flag_w = False
flag_c = False
files = []

for arg in args:
    if arg == "-l":
        flag_l = True
    elif arg == "-w":
        flag_w = True
    elif arg == "-c":
        flag_c = True
    else:
        files.append(arg)

no_flags = not flag_l and not flag_w and not flag_c

total_lines = 0
total_words = 0
total_bytes = 0

for file in files:
    with open(file, "r") as f:
        content = f.read()
    byte_count = os.path.getsize(file)
    line_count = content.count("\n")
    word_count = len(content.split())

    total_lines += line_count
    total_words += word_count
    total_bytes += byte_count

    parts = []
    if flag_l or no_flags:
        parts.append(f"{line_count:>8}")
    if flag_w or no_flags:
        parts.append(f"{word_count:>8}")
    if flag_c or no_flags:
        parts.append(f"{byte_count:>8}")
    parts.append(f" {file}")
    print("".join(parts))

if len(files) > 1:
    parts = []
    if flag_l or no_flags:
        parts.append(f"{total_lines:>8}")
    if flag_w or no_flags:
        parts.append(f"{total_words:>8}")
    if flag_c or no_flags:
        parts.append(f"{total_bytes:>8}")
    parts.append(" total")
    print("".join(parts))