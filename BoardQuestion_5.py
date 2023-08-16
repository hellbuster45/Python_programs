n = int(input("Enter any positive integer: "))

s = 0 
for i in range(1, n+1):
    s += i
    
print("Sum of series till",n, "is: ",s)