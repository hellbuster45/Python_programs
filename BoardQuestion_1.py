#Question 9
name = input("Enter name: ")
roll = input("Enter roll no.: ")
age = int(input("Enter age: "))
Pmarks = eval(input("Enter physics marks: "))
Cmarks = eval(input("Enter chemistry marks: "))
Mmarks = eval(input("Enter maths marks: "))
print("Name: ", name)
print("Roll No.: ", roll)
print("Age: ", age)
print("Physics: ", Pmarks)
print("Chemistry", Cmarks)
print("Maths", Mmarks)
print("Total: ", (Pmarks + Cmarks + Mmarks), "Average: ", (Pmarks + Cmarks + Mmarks)/3)