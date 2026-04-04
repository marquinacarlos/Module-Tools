import sys
import os

args = sys.argv[1:]

flag_n = False
flag_b = False
files = []

for arg in args:
    if arg == "-n":
        flag_n = True
    elif arg == "-b":
        flag_b = True
    else:
        files.append(arg)

line_number = 1

for file in files:
    with open(file, "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.rstrip("\n")
        if flag_b:
            if line == "":
                print("")
            else:
                print(f"     {line_number}\t{line}")
                line_number += 1
        elif flag_n:
            print(f"     {line_number}\t{line}")
            line_number += 1
        else:
            print(line)