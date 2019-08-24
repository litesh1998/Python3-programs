import argparse

ps=argparse.ArgumentParser(description='This program displace the the square value of given number')

ps.add_argument('num',type=int,help='Please Enter Integer Type Number')

args=ps.parse_args();
result=args.num**2
print('Square Vslue= ', result)