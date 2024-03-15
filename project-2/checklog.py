#!/usr/bin/python3

import sys
import hashlib
import base64

if len(sys.argv) > 1:
    print("Usage: checklog", file = sys.stderr)
    exit(1)

try: 
    log = open("log.txt", "r")

except:
    print("Error: log.txt not found.")
    exit(1)

try:
    loghead = open("loghead.txt", "r")

except:
    print("Error: loghead.txt not found.")
    exit(1)

log = open("log.txt", "r")
first_line = log.readline()
if first_line.split()[2] != "begin":
    print("failed")

sha256_hash = hashlib.sha256(first_line.encode()).digest()
base64_encoded_hash = base64.b64encode(sha256_hash).decode()

line = log.readline()
while line:
    print(line)
    line = log.readline()