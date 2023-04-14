mass = float(input('enter the weight in kg: '))
height = float(input('enter the height in metres: '))

BMI = (mass)/(height*height)

text = 'Your BMI is: '

print(text,BMI)

a = float(24.9)

if BMI > a:
 print('You are overweight')

 b =float(18.9)

 if BMI < b:
   print('You are underweight')

c = float(30.9)

if BMI > c:
  print('No offense your are obese')

else:
  print('You are weight is perfect')


