print(" enter the employee salary :")
s=float(input())
if s>=5000:
	da=s*0.7
	hra=s*0.5
else :
	da=s*0.4
	hra=s*0.3
total=s+da+hra	
print("salary is",s)
print("da is",da)
print("hra is",hra)
print("total salary of the employee :",total)