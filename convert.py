# python program to convert into decimal number system
n1= 0o27
n2=0b111101011
n3=0x1d2
print("octal 27=", n1)
print("Binary 111101011=",n2)
print("hexadecimal 1d2=",n3)
"""
Result:
Pyhon always saves the numbers as numeric values.
to print in another format you have to use type conversion.
"""
s="10111"
n=int(s,2)
print(s)
print(n)