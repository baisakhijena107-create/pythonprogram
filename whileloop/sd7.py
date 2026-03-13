print("enter a number")
n=int(input())
l=n%10
while n!=0:
	r=n%10
	n=n//10
print("sum of first and last digit is :",r+l)