#Question 10

x,y,z = eval(input('Enter any three numbers seperated by commas: '))

if x > y:
    if x > z:
        print(x, 'is the maximum')
    else:
        print(z, 'is the maximum')
else:
    if y > z:
        print(y, 'is the maximum')
    else:
        print(z, 'is the maximum')