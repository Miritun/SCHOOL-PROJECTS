firstName = str(input("Write your First Name: "))
print("\n")

lastName = str(input("Write your Last Name: "))
print("\n")

location = str(input("Enter your Location: "))
print("\n")

age = str(input("Enter your Age: "))
print("\n")

info = [firstName, lastName, location, age]
display = []
space = " "

for check in range(4):
    if info[check] == "":
        display.append("/Invalid or Missing/")
    else:
        display.append(info[check])

print(display[0] + space + display[1] + space + display[2] + space + display[3] + space)
