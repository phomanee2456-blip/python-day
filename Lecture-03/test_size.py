num_employees = int(input("Enter the number of employees: "))

#size
if num_employees < 50:
    print("this is a small company.")
elif num_employees < 250:
    print("This is a medium-sized company. ")
elif num_employees >= 250:
    print("This is a large company. ")