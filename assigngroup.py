#!/usr/bin/env python3
groupsize = 82
count = 0
pair = 0

file = open("class2018.csv",'r')

for f in file:
	field = f.split(",")
	if count < groupsize:
		group = "A"
	elif count < groupsize * 2:
		group = "B"
	else:
		 group = "C" 
	pair = int(count / 2 + 1)
	print(group +  str(pair),", ",  field[0],",",field[1],", ",field[2],sep="")
	count = count + 1
