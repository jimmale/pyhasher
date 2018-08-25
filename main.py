#!/usr/bin/env python3
import os
import hasherfile
from functools import reduce
from concurrent import futures
from tqdm import tqdm

path = "/Users/jim/Music/"

# recursively lists all files in the path
def listFiles(path):
    output = []
    for path, directories, files in os.walk(path):
        for file in files:
            filePath = os.path.join(path, file)
            f = hasherfile.hasherfile(filePath)
            output.append(f)
    return output

files = listFiles(path)

# Get the total data volume to be hashed
sizes = map(lambda x: x.getSize(), files)
sum = reduce((lambda x, y: x + y), sizes)

# set up a thread pool.
# I played around with the max_workers parameter and 4 seems best for my mbp
pool = futures.ThreadPoolExecutor(max_workers=4)

# Set up a progress bar
pbar = tqdm(total=sum, unit='B', unit_scale=True)

# helper functions to work with tqdm from different futures

# do the file hashing and then return the number of bytes that were hashed
def doHash(f):
    f.getHash()
    return f.getSize()

# increment the progress bar's count of bytes that have been hashed
def bump(x):
    pbar.update(x.result())

# for each file
for file in files:
    # submit it to the thread pool and get notified when it's done
    future = pool.submit(doHash, file)
    future.add_done_callback(bump)

# write the results
fout = open("hashes.sha1", "w")
for file in sorted(files):
    fout.write(file.getHash() + " " + file.getPath() + "\n")
