a=int(input("enter first number"))
b=int(input("enter second number"))
for n in range (a,b,1):
	s=0
	for d in range(1,n//2+1,1):
		if n%d==0:
			s=s+d
	if n==s:
		print(n,"is perfect number")
