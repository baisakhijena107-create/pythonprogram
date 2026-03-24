s = "Ram                                                                                          "
print(len(s))
c=0
for i in range (len(s)-1,0,-1):
    if s[i]==" ":
        c=c+1
    else:
        break
print(len(s[0:len(s)-c]))