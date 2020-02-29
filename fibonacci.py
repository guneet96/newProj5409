import datetime
import time
f = open("input.txt", "r")
fo = open("out_fibo.csv", "w")

for num in f:
	num = num.strip()
	f0 = 0
	f1 = 1
	
	if num == 1:
		t1 = datetime.datetime.now()
		print(f0)
		t2 = datetime.datetime.now()
		#fo.write(str(num) + "," +str(t2-t1) + "\n")
	if num == 2:
		t1 = datetime.datetime.now()
		print(str(f0) + " " + str(f1))
		t2 = datetime.datetime.now()
		#fo.write(str(num) + "," +str(t2-t1) + "\n")
	else:
		t1 = datetime.datetime.now()
		#t3 = datetime.datetime.now()
		print(str(f0) + " " + str(f1) + " ")
		for i in range(3,int(num)+1):
			fn = f0+f1
			#print(str(fn) + " ")
			f0 = f1
			f1 = fn
			print(fn)
		#t4 = datetime.datetime.now()
		#fo.write(str(num) + "," +str(t4-t3) + "\n")
		
		t2 = datetime.datetime.now()
	print(t2-t1)
	d = str(t2-t1)
	fo.write(str(num) + "," + d + "\n")
f.close()
fo.close()
