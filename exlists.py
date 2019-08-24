d,n,m=map(int, input().split(' '))
k=list(map(int, input().split(' ')))
u=list(map(int, input().split(' ')))

k.sort(reverse=True)
u.sort(reverse=True)

s=ts=i=j=0
while i<n and j<m:
    ts=k[i]+u[j]
    if ts<d:
        s=ts
        print(ts)
        break
    elif k[i+1]>u[j+1]:
        i=i+1
    elif u[j+1]>k[i+1]:
        j=j+1
if s==0:
    print(-1)