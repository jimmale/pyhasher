import hashlib
import os

class hasherfile:
    size = -1
    sha1hash = ""
    path = ""

    def __init__(self, path):
        self.path = path

    def __lt__(self, other):
     return self.path < other.path
     
    def getSize(self):
        if (self.size is -1):
            self.size = os.path.getsize(self.path)
        return self.size

    def getHash(self):
        if (self.sha1hash is ""):
            m = hashlib.sha1()
            f = open(self.path, "rb")
            m.update(f.read())
            f.close()
            self.sha1hash = m.hexdigest()
        return self.sha1hash

    def getPath(self):
        return self.path
