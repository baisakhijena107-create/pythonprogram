n=11
c=0
for d in range(2,n//2+1,1):
	if n%d==0:
		c=c+1
if c==0:
	print(n,"is prime number")
else:
	print(n,"is not prime number")