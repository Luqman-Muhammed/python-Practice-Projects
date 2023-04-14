height = int(input('Enter the height: '))
credits = int(input('Enter the credits you have: '))

if height >= 137 and credits >= 10:
    print('You can enjoy the ride')

elif height < 137:
    print('You are not tall enough')

elif credits < 10:
    print('You dont have enough credits')

else:
    print('invalid data')


