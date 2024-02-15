#!/usr/bin/python3

import sys
import math

def fill_table(empty_table, data_list):
    #print(table_size, blocksize[1])
    difference = table_size - blocksize[1]
    if difference > 0:
        i = len(key) - 1
        j = rows - 1
        counter = 0
        while j >= 0:
            while i >= 0:
                if counter == difference:
                    break
                else:
                    empty_table[j][i] = 0
                    counter += 1
                i -= 1
            j -= 1

    #print(empty_table)

    sorted_key = sorted(key)
    prev = ""
    counter = 0
    for char in sorted_key:
        if char == prev:
            prev_index = key.index(prev)
            for i in range(rows):
                if empty_table[i][key.index(char, prev_index + 1)] != 0:
                    empty_table[i][key.index(char, prev_index + 1)] = data_list[counter]
                    counter += 1

            #print(key.index(char, prev_index + 1))
        else:
            for i in range(rows):
                if empty_table[i][key.index(char)] != 0:
                    empty_table[i][key.index(char)] = data_list[counter]
                    counter += 1
            #print(key.index(char))
        prev = char 

    if difference > 0:
        y = len(key) - 1
        z = rows - 1
        counter = 0
        while z >= 0:
            while y >= 0:
                if counter == difference:
                    break
                else:
                    empty_table[z][y] = b''
                    counter += 1
                y -= 1
            z -= 1

    #print(empty_table)
    return empty_table

def print_table(table):
    for i in range(rows):
        for j in range(len(key)):
            print(table[i][j].decode('ascii', errors='replace'), end="")

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

rows = math.ceil(blocksize[1] / len(key))

table = [[0 for i in range(len(key))] for j in range(rows)]

f = open(file, mode="rb")

rows = math.ceil(blocksize[1] / len(key))

table = [[b'' for i in range(len(key))] for j in range(rows)]
table_size = len(key) * rows

counter = 0
data_list = [b'' for i in range(table_size)]
data = f.read(1)
data_list[counter] = data
#print(data_list)
counter += 1
while data:
    if counter == blocksize[1]:
        table = fill_table(table, data_list)
        counter = 0
        #print("here")
        print_table(table)
        data_list = [b'' for i in range(table_size)]
        table = [[b'' for i in range(len(key))] for j in range(rows)]
    else:
        data = f.read(1)
        data_list[counter] = data
        counter += 1
        #print(data_list)

# decrypt what is leftover in table
table = fill_table(table, data_list)
print_table(table)