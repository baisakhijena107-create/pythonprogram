print("enter a number")
n=int(input())
if n%35==0:
    print("number is divisible by both 5 and 7")
elif n%5==0:
    print("number is divisible by 5 ")
elif n%7==0:
    print("number is divisible by 7")
else:
    print("number is not divisible by 5 or 7")