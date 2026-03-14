print("enter a number")
n=int(input())
es,os,oc,ec=0,0,0,0
while n!=0:
	r=n%10
	if n%2==0:
		es=es+r
		ec=ec+1
	else:
		os=os+r
		oc=oc+1
	n=n//10
print ("number of odd digit:",oc)
print ("number of even digit:",ec)
print ("sum of odd digit:",os)
print ("sum of even digit:",es)