n = int(input("Enter any positive integer: "))

s = 0
for i in range(2, n+1, 2):
  s += i**2

print("Sum of series till",n, "is: ",s)