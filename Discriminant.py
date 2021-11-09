a = int(input ("Введите a: "))
b = int(input ("Введите b: "))
c = int(input ("Введите c: "))
D = b**2-4*a*c
if D>0:
    X1=( -b+D**0.5)/(2*a)
    X2=( -b-D**0.5)/(2*a)
    print ("Корни уравнения: ", X1,X2)
if D==0:
    X = (-b)/(2*a)
    print ("Корень уравнения: ", X)
if D < 0:
    print ("Корней нет")
