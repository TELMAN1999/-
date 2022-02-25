import os
import json

path = os.path.abspath('dir1')

mydict = {}
mylist = ["telman", "ani","davit"]

def obxodFile(path, level=1):
    for i in os.listdir(path):
        if os.path.isfile(path + '/' + i):
            with open(path + "/" + i, 'r') as f:
                text = f.read()
                for j in text.split():
                    if j.find('@') != -1:
                        for k in mylist:
                            if k in j :
                                mydict[k] = j
        if os.path.isdir(path + '/' + i):
            obxodFile(path + '/' + i, level + 1)
obxodFile(path)
y = json.dumps(mydict)
print(y)
