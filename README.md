##pyhasher
A quick Python 3 script to traverse a directory and perform a SHA1 hash on each of the files and save the output.

Useful for checking for corruption when moving important files from one system to another.

#### running
```
virtualenv -p python3 venv
source ./venv/bin/activate
pip install -r ./requirements.txt
./main.py
```

#### FAQs
```
Q: Is this a shining example of your best work?
A: No. I threw this together in under an hour and spent a good amount of time
just learning about how to do multithreading in python.

Q: It's multithreaded?
A: Yes, but it's hardcoded for 4 threads.

Q: How fast is it?
A: It's hashing a little under 500MB/s on my system. YMMV.

Q: Why did you do this?
A: I need to back up my music to an external hard drive before reformatting my
mac and don't want to risk some files getting corrupted in the process

Q: Are there any easter eggs?
A: No.
```
