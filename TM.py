import os
import json
import re


email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

path = os.path.abspath('dir1')

sinvol = [':', '-','_', '`', '~', '!', '#', '$', '%', '^', '*', '(' , ')', '=', '+', '/', '|', '.']
mydict = {}

def filersearch(text):
    name, pos_sin, pos = None, None, None
    for mail in text.split():
        if email_regex.match(mail) != None:
            pos = mail.find("@")
            for k in sinvol:
                if k in mail:
                   pos_sin = mail.find(k)
                   return mail, pos_sin, pos
    return mail, pos_sin, pos

def obxodFile(path, level=1):
    for i in os.listdir(path):
        if os.path.isfile(path + '/' + i):
            with open(path + "/" + i, 'r') as f:
                text = f.read()
                mail, pos_sin, pos = filersearch(text)
                if mail and pos_sin and pos:
                    name = mail[pos_sin+1:pos]
                    F_mail = mail.split()
                    mydict[name] = F_mail

        if os.path.isdir(path + '/' + i):
            obxodFile(path + '/' + i, level + 1)
obxodFile(path)
d_json = json.dumps(mydict)
my_file = open("File.json", "w+")
my_file.write(d_json)
my_file.close()
