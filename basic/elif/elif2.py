print("enter a number")
n=int(input())
if n<10:
	print("the number is single digit")
elif n<100:
	print("the number is double digit")
elif n<1000:
	print("the number is triple digit")
else :
	print("the number is other")