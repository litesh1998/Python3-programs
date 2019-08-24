s=input().strip()
l=[]
for i in range(len(s)):
       l.append(int(s[i]))
if (l.count(1)==1) or (l.count(0)==1):
  print("YES",end='')
else:
  print("NO",end='')