n = int(input("Enter the number of stars at pyramid peak: "))

for i in range(n):
    print('*' * (i+1))

for i in range((n-1),0,-1):
    print('*' * i)