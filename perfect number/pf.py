n=int(input("enter a number"))
s=0
for d in range(1,n//2+1,1):
	if n%d==0:
		s=s+d
if n==s:
	print(n,"is perfect number")
else:
	print(n,"is not perfect number")