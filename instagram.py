import sys, os
import json
import subprocess
from types import coroutine

with open('message_1.json') as file: #se lee el archivo
  input_json = json.loads(file.read()) #se lo guarda en la variable input_json

author = [] #se crean un par de arrays para informacion
msg = []
for data in input_json["messages"]: #por cada mensaje
    author.append(data["sender_name"]) #se checkea el nombre del "sender" y se lo guarda en la array author
    if "content" in data: #si hay content (el texto de un msg) se lo guarda en msg
        msg.append(data["content"])
    elif "audio_files" in data: #si hay audio se checkea uri (la localizacion del archivo) y se lo guarda en msg
        for f in data["audio_files"]:
            msg.append(f["uri"])
    elif "share" in data: #si es un link se lo guarda tambien en msg
        msg.append(data["share"]["link"])
    elif "photos" in data:
        for f in data["photos"]: #La localizacion de imagnes reciven el mismo tratado que los audios
            msg.append(f["uri"])

subprocess = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE) #se lee la salida del "dir"
folder = subprocess.stdout.read()
folder = str(folder) #se guarda la salida

x = folder.find(":\\\\") #se recorta la localizacion del script
folder = folder[x-1:]
y = folder.find("\\r")
folder = folder[:y] #se la guarda en folder




counter = 0
author = author[::-1] #se invierten las arrays
msg = msg[::-1]
print("msg:",len(msg)) #debug
print("autor:",len(author)) #debug
print("data:", len(input_json["messages"])) #debug
for a in author:
    print(a+":"+" "+msg[counter]) #se imprimen los msg
    counter = counter+1
