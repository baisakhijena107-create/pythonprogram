print("enter a number")
n=int(input())
oc=0
ec=0
while n!=0:
	r=n%10
	if n%2==0:
		ec=ec+1
	else:
		oc=oc+1
	n=n//10
print ("number of odd digit:",oc)
print ("number of even digit:",ec)