c=1
for a in range(4,0,-1):
	for b in range (1,a+1,1):
		print(b,end="")
	if a==4:
		for b in range(a-1,0,-1):
			print(b,end="")
		print()
		continue
	for b in range (0,c,1):
		print(end=" ")
	for b in range(a,0,-1):
		print (b,end="")
	c=c+2
	print()