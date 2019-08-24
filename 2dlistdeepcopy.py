import copy
l=[[1,2,3],[4,5,6]]
#l2=[x.copy() for x in l]
l2=copy.deepcopy(l)
l2[1][2]=100
print(id(l))
print(id(l2))
print(l)
print(l2)