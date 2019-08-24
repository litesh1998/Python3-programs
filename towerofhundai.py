def towers(n, scource, destination, spare):
    '''Recursive Functio To solve Tower of Hanoi '''
    if n == 1:
        print('Move block %i from %s to %s' % (n, scource, destination))
    else:
        towers(n-1, scource, spare, destination)
        print('Move block %i from %s to %s' % (n, scource, destination))
        towers(n-1, spare, destination, scource)


towers(int(input('Enter the No of Blocks')), 'A', 'B', 'C')
