space = " "

firstName=str(input("Write your First Name: "))

lastName=str(input("Write your Last Name: "))

location=str(input("Enter your Location: "))

age=str(input("Enter your Age: "))

info = [firstName,lastName, location,age]

check = 0

for check in range(4):
    
    if info[check]=="":
        print("Invalid/Missing!"+ space, end="")
    else:
        print(info[check] + space, end= "")
   