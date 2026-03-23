n=145
s=0
temp=n
while temp>0:
	r=temp%10
	f=1
	while r>0:
		f=f*r
		r=r-1
	s=s+f
	temp=temp//10
if n==s:
	print(n,"is strong number")
else:
	print(n,"is not strong number")