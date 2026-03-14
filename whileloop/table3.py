print("enter a number")
a=int(input())
for i in range(1,4,1):
	for b in range (1,11,1,):
		if i==1:
			print(a*b,end="\t")
		elif i==2:
			print(b,end="\t")
		else:
			print(a,end="\t")
	print()