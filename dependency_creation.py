#!/usr/bin/env python3

f = open("input.txt", "w")
for i in range(1,101):
	#print(str(i))
	f.write(str(i) + "\n")

f.close()
