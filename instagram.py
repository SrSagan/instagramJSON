import sys, os
import json
import subprocess
from types import coroutine

with open('message_1.json') as file:
  input_json = json.loads(file.read())

author = []
msg = []
for data in input_json["messages"]:
    author.append(data["sender_name"])
    if "content" in data:
        msg.append(data["content"])
    elif "audio_files" in data:
        for f in data["audio_files"]:
            msg.append(f["uri"])
    elif "share" in data:
        msg.append(data["share"]["link"])
    elif "photos" in data:
        for f in data["photos"]:
            msg.append(f["uri"])

subprocess = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE) #se lee la salida del comento	
folder = subprocess.stdout.read()
folder = str(folder)

x = folder.find(":\\\\")
folder = folder[x-1:]
y = folder.find("\\r")
folder = folder[:y]




counter = 0
author = author[::-1]
msg = msg[::-1]
print("msg:",len(msg))
print("autor:",len(author))
print("data:", len(input_json["messages"]))
for a in author:
    print(a+":"+" "+msg[counter])
    counter = counter+1
