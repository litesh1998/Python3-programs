import sys

n=len(sys.argv)
argv=sys.argv
argv[0]=0;
print('No of arguments are= ',n)
for int(x) in argv: print(x)