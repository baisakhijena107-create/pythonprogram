s = "        Ram"
c = 0
for i in s:
    if i==" ":
        c=c+1
        continue
    else:
        break

print(s[c:])