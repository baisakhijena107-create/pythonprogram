a=0
for n in range(1,1001,1):
	s=0
	for d in range(1,n//2+1,1):
		if n%d==0:
			s=s+d
	if n==s:
		a=a+n
		print(n,"is perfect number")
print("sum of perfect number :",a)