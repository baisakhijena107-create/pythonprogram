for a in range (1,5,1):
	for b in range (1,a+1,1):
		if a%2==0:
			print("#",end="\t")
		else:
			print("@",end="\t")
	print()
