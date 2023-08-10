#Question 14

num = int(input('Enter any four digit integer: '))
div = 1000
rem = 0
rev = 0
i = 1

while div != 0:
    rem = num // div
    num = num - (rem * div)
    rev = rev + (rem * i)
    div = div // 10
    i = i * 10
print('Reverse number is: ', rev)