a = int(input("Enter no with x*x : "))
b = int(input("Enter no with x : "))
c = int(input("Enter no with no x : "))

quad_eq1 = (-b + (b*b - 4*a*c)**0.5 )/ (2*a) 
quad_eq2 = (-b - (b*b - 4*a*c)**0.5 )/ (2*a) 

qd = 'Quadratic equartions are: '

print(qd,quad_eq1)
print(quad_eq2)


