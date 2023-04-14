import math


a = int(input('Enter a the length of height side: '))
b = int(input('Enter a the length of base side: '))

Baseside = a*a
Heightside = b*b
Hypotenuse = Baseside + Heightside

hyp = 'Hypotenuse is: '

print(hyp,math.sqrt(Hypotenuse))


