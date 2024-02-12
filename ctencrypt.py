#!/usr/bin/python3

import sys
import math

tag_1 = sys.argv[1]
content_1 = sys.argv[2]

blocksize = [False, 16]
key = ""
file = ""

if (tag_1 == "-b"):
    try:
        blocksize[1] = int(content_1)
        blocksize[0] = True

        key = sys.argv[4]
        file = sys.argv[5]

    except ValueError:
        print(ValueError.__name__, file=sys.stderr)

elif (tag_1 == "-k"):
    key = content_1
    file = sys.argv[3]

f = open(file, mode="rb")

rows = math.ceil(blocksize[1] / len(key))
table = [[0 for i in range(len(key))] for j in range(rows)]

for i in range(rows):
    for j in range(len(key)):
        print(i, j)
        data = f.read(1)
        table[i][j] = data

sorted_key = sorted(key)
print(sorted_key)
for char in sorted_key:
    print(key.index(char)) 
