for a in range(68,64,-1):
	for b in range(68-a,0,-1):
		print(end=" ")
	for b in range(65,a+1,1):
		print(chr(b),end="")
	for b in range(a,64,-1):
		print(chr(b),end="")
	print()