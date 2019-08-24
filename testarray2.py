#from array import *
str=input('Enter The Marks : ').split(' ')
marks=[int(num) for num in str]
print(marks)
sum=0
n=len(marks)
for i in marks:
    sum+=i
percent=sum*100/(n*10)
print('Sum is ',sum,'Percentage Is ',percent,'%')
print(marks[1])