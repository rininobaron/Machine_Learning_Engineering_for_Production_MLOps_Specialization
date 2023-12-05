#! /usr/bin/env python3

import os

files = os.listdir("/home/ricardo/anaconda3/pkgs")

suma1=0
suma2=0
for file in files:
	print(file)
	if file[-5:]=="conda":
		suma1 += 1
	else:
		suma2+=1
print(suma1)
print(suma2)