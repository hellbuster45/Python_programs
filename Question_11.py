#Question 11
import math as m
import random as r
lott_number = int(r.randrange(10,100))
print(lott_number)

fir_dig = m.floor(lott_number / 10)
sec_dig = lott_number - (fir_dig * 10)

rev_num = (sec_dig * 10) + fir_dig
print(rev_num)

u_input = int(input('Enter any two digit number: '))

if u_input == lott_number:
    print('You won $10000!!')
elif u_input == rev_num:
    print('You won $3000!!')
elif (m.floor(u_input / 10) == fir_dig) or (m.floor(u_input / 10) == sec_dig):
    print('You won $1000!!')
else:
    print('You won nothing!!')