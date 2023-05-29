import json
import socket
import threading
import time
import os
import requests

ip = []
port = []
name = []
protocol = []
ipv = []

with open("config.json") as c:
    cd = json.load(c)

user_id = cd['user_id']
url = cd['url']

data = {
    "username" : "SEE ALL",
    "avatar_url" : "https://png2.cleanpng.com/sh/2d60ee9fb2d434f37956b1394291ffef/L0KzQYm3UsE3N5t5fZH0aYP2gLBuTfNwdaF6jNd7LX3yfrr7jCIudZDzgeZ4cnnxd376mgN1bZ4yhdH3aYTygn7qjPlxNZJ3RdV4bYD4hLb5TgRwd50ye95ycHH1hMS0VfE5P2E5T9YEZXLpdIG1U8Y3PmU1SqQ6NUG7R4qAWcQ6PmY1S5D5bne=/kisspng-computer-monitor-monitoring-system-monitor-clip-ar-computer-tool-cliparts-5a87047d9ebfd0.3666402215187979496503.png"
}

with open("data.json") as f:
    d = json.load(f)
    for i in range(0, len(d)):
        ip.append(d[i]['ip'])
        port.append(d[i]['port'])
        name.append(d[i]['name'])
        protocol.append(d[i]['protocol'])
        ipv.append(d[i]['ipv'])

def tcp(v):
    if v == 4:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    elif v == 6:
        s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.settimeout(5)
    res(s)

def udp(v):
    if v == 4:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    elif v == 6:
        s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    s.settimeout(5)
    res(s)

def res(s):
    try:
        conn = s.connect_ex((ip[i], port[i]))
        if not conn:
            print(f"The device with name {name[i]} which has ip {ip[i]} and port {port[i]} is Active right now")
        else:
            print(f"The device with name {name[i]} which has ip {ip[i]} and port {port[i]} is InActive right now")
            if cd['discord'] == "True":
                data["content"] = f"<@{user_id}>\nThe device with name `{name[i]}` which has ip `{ip[i]}` and port `{port[i]}` is `InActive` right now"
                requests.post(url, json = data)
        s.close()
    except socket.gaierror:
        print(f"Someting is wrong in your data.json file with {name[i]}")

def see(i):
    if protocol[i] == "tcp" or protocol != "udp":
        if ipv[i] == "4" or ipv[i] != "6":
            tcp(4)
        elif ipv[i] == "6":
            tcp(6)
    elif protocol[i] == "udp":
        if ipv[i] == "4" or ipv[i] != "6":
            udp(4)
        elif ipv[i] == "6":
            udp(6)

while True:
    for i in range(0, len(ip)):
        thread = threading.Thread(target=see, args=(i,), daemon=True).start()
        time.sleep(0.01)
    time.sleep(cd['intervel'])
    print("-"*80)