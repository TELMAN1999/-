import os
import json
import re


email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

path = os.path.abspath('dir2')

simvol = [':', '-','_', '`', '~', '!', '#', '$', '%', '^', '*', '(' , ')', '=', '+', '/', '|', '.']
mydict = {}
F_lst = []

def filersearch(text):
    name, pos_sin, pos = None, None, None
    for mail in text.split():
        if email_regex.match(mail) != None:
            pos = mail.find("@")
            for k in simvol:
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
                    spl_mail = mail.split(name)
                    F_mail = spl_mail[0]+spl_mail[1]
                    lst = F_mail.split()
                    mydict[name] = lst
        if os.path.isdir(path + '/' + i):
            obxodFile(path + '/' + i, level + 1)

def MySortDict(mydict):
    vel = sorted(mydict)
    for i in range(len(mydict)):
        NewDict = {}
        key = vel[i]
        NewDict[key] = mydict[key]
        F_lst.append(NewDict)

obxodFile(path)
MySortDict(mydict)
d_json = json.dumps(F_lst)
my_file = open("File.json", "w+")
my_file.write(d_json)
my_file.close()
