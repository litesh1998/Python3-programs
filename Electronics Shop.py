d, n, m = map(int, input().split(' '))
k = list(map(int, input().split(' ')))
u = list(map(int, input().split(' ')))

k.sort(reverse=True)
u.sort(reverse=True)
s = []

for i in k:
    for j in u:
        s.append(i+j)
s.sort(reverse=True)
for i in s:
    if i <= d:
        print(i)
        break
