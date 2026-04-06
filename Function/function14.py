def si(p,r,t):
	s=p*r*t/100
	return s
p=int(input("enter the principal amount"))
r=int(input("enter the rate of interest"))
t=int(input("enter the time"))
res=si(p,r,t)
print("simple interest=",res)