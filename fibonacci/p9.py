c=1
d=0
for a in range (1,5,1):
	d=c+a
	for b in range (1,a+1,1):
		if a%2==0:
			d=d-1
			print(d,end="\t")
		else:
			print(c,end="\t")
		c=c+1
	print()    
