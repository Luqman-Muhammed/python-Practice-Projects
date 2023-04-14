ph = int(input('Enter the Ph value of the solution: '))

if ph < 7:
    print('The solution is acidic')
elif ph > 7:
    print('The solution is basic')
else:
    print('The solution is neutral')

