#Question 10
eName = input("Enter employee name: ")
email = input("Enter email ID: ")
design = input("Enter designation: ")
code = input("Enter empoyee code: ")
salary = eval(input("Enter employee salary: "))

PF = (12*salary)/100
DA = (18*salary)/100
HRA = (10*salary)/100
IT = (9*salary)/100
NetPay = salary + DA + HRA - (PF + IT)

print("**************Birla Institute of Technology*****************\n\n")
print("Name: ", eName, "\t empCode: ", code, "\t Designation: ", design, "\n Salary: ", salary, "\t email ID: ", email)
print("\n\nPF: ", PF, "\t DA: ", DA, "\t HRA: ", HRA, "\n IT: ", IT, "\t Netpay: ", NetPay)