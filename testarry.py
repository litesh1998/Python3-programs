import array as ar
a=ar.array('i',[2,5,7,6])
for i in a[-3:]:
    print(i,end='\t')
else:
    print()
a.append(54)
print(a)
b=[1,3,99]
a.extend(b)
print(a)