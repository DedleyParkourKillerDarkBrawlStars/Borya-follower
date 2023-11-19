import math
a=float(input('Input a: '))
b=float(input('Input b: '))
c=float(input('Input с: '))
if a<0 or b<0 or c<0 or a+b<c or a+c<b or b+c<a:
    print("Невозможный треугольник")
else:
    p = (a+b+c)/2
    S=math.sqrt (p*(p-a)*(p-b)*(p-c))
    print ('Площадь треугольника составляет:',S)