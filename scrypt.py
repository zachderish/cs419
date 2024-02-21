#!/usr/bin/python3

import sys

def sdbm(string):
    hash = 0
    for char in string:
        hash = ord(char) + (hash << 6) + (hash << 16) - hash
    return hash

def keystream(seed):
    #print(seed)
    next_num = (1103515245 * seed + 12345) % 256
    return next_num


password = sys.argv[1]

text1 = sys.argv[2]
text2 = sys.argv[3]

file1 = open(text1, mode="rb")
file2 = open(text2, mode="w")


key = sdbm(password)
char = file1.read(1)

while char:
    #print(key)
    key = keystream(key)
    #key_string = str(key)
    #key_encoded = key_string.encode()
    char_int = int.from_bytes(char, "little")
    print(char_int, key)
    #cipher_char = bytes((a ^ b) for a, b in zip(char, key_encoded))
    cipher_char = key ^ char_int
    print(cipher_char)
    if 0 <= cipher_char <= 127:
        cipher_char = chr(cipher_char)
        file2.write(cipher_char)
    else:
        file2.write('\uFFFD')
    #cipher_char = cipher_char.decode('ascii', errors='replace')
    #cipher_char = str(cipher_char)
    char = file1.read(1)

print(bytes((a ^ b) for a, b in zip(b'T', b'150')))
print(150 ^ 1010100)