print("enter the term")
t=int(input())
print("enter the frist number")
a=int(input())
print("enter second number")
b=int(input())
print(a,b,end="\t")
while t>2:
	c=a+b
	print(c,end="\t")
	a=b
	b=c
	t=t-1