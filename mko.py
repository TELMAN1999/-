import os
import json
import re


email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

path = os.path.abspath('dir2')

sinvol = ['.', ':', '-','_', '`', '~', '!', '#', '$', '%', '^', '*', '(' , ')', '=', '+', '/', '|' ]
mydict = {}
mylist = ["telman", "ani","davit"]

def obxodFile(path, level=1):
    for i in os.listdir(path):
        if os.path.isfile(path + '/' + i):
            with open(path + "/" + i, 'r') as f:
                text = f.read()
                for j in text.split():
                    if email_regex.match(j) != None:
                        print(j)
                        p= j.find('@')
                        print(p)
                        for k in sinvol:
                            if k in j:
                                o = j.find(k)
                                print(o)
                                break
                        a = j[o+1:p]
                        print(a)
                        x = j.split()
                        print(x)
                        mydict[a] = x
        if os.path.isdir(path + '/' + i):
            obxodFile(path + '/' + i, level + 1)
obxodFile(path)
y = json.dumps(mydict)
print(y)
my_file = open("File.json", "w+")
my_file.write(y)
my_file.close()
