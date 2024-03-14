#!/usr/bin/python3

import sys
import hashlib
import base64
import datetime

if(len(sys.argv) != 2):
    print("Usage: addlog log_string", file = sys.stderr)
    exit(1)

try: 
    log = open("log.txt", "r")

except:
    log = open("log.txt", "w")
    log_head = open("loghead.txt", "w")
    log_head.write("begin")

try:
    log_head = open("loghead.txt", "r")

except:
    print("loghead.txt does not exist", file = sys.stderr)
    exit(1)

log_head = open("loghead.txt", "r")
hash = log_head.read()

datetime_precision = datetime.datetime.now()
datetime_without_prec = datetime_precision.strftime('%Y-%m-%d %H:%M:%S')

log_line = f"{datetime_without_prec} {hash} {sys.argv[1]}\n"
log = open("log.txt", "a")
log.write(log_line)

log_line = log_line.replace('\n', '')
sha256_hash = hashlib.sha256(log_line.encode()).digest()
base64_encoded_hash = base64.b64encode(sha256_hash).decode()
log_head = open("loghead.txt", "w")
log_head.write(base64_encoded_hash)


