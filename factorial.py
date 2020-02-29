#!/usr/bin/env python3

import datetime
import time

f = open("input.txt", "r")
fo = open("fac_out.csv", "w")
for num in f:
	num = num.strip()
	n = int(num)
	temp = n
	fac = 1
	t1 = datetime.datetime.now()
	while(temp>=1):
		fac = fac*temp
		temp=temp-1
	t2 = datetime.datetime.now()
	w = str(num) + "," + str(t2-t1) + "," + str(fac) + "\n"
	fo.write(w)
f.close()
fo.close()
