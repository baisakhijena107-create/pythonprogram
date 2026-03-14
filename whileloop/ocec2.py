print("enter a number")
n=int(input())
os=0
es=0
while n!=0:
	r=n%10
	if n%2==0:
		es=es+r
	else:
		os=os+r
	n=n//10
print ("sum of odd digit:",os)
print ("sum of even digit:",es)