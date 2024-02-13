#!/usr/bin/python3

import sys
import math

def encrypt(table):

    print(table)

    sorted_key = sorted(key)
    #print(sorted_key)
    prev = ""
    final_output = ""
    for char in sorted_key:
        if char == prev:
            prev_index = key.index(prev)
            for i in range(rows):
                print((table[i][key.index(char, prev_index + 1)]).decode('ascii', errors='replace'), end="")

            #print(key.index(char, prev_index + 1))
        else:
            for i in range(rows):
                print((table[i][key.index(char)]).decode('ascii', errors='replace'), end="")
            #print(key.index(char))
        prev = char 

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
table_size = len(key) * rows

for i in range(rows):
    for j in range(len(key)):
        #print(i, j)
        data = f.read(1)
        table[i][j] = data

encrypt(table)



f.close()
exit()

for i in range(rows):
    for j in range(len(key)):
        #print(i, j)
        data = f.read(1)
        table[i][j] = data

#print(table)

sorted_key = sorted(key)
#print(sorted_key)
prev = ""
final_output = ""
for char in sorted_key:
    if char == prev:
        prev_index = key.index(prev)
        for i in range(rows):
            print((table[i][key.index(char, prev_index + 1)]).decode('ascii', errors='replace'), end="")

        #print(key.index(char, prev_index + 1))
    else:
        for i in range(rows):
            print((table[i][key.index(char)]).decode('ascii', errors='replace'), end="")
        #print(key.index(char))
    prev = char 
