# Create an empty dictionary
employees = {}

# infinite while loop
while True:
    # input name of employee
    name = input("Enter name of employee: ")
    # input salary of employee
    salary = input("Enter salary of employee: ")
    # store name and salary in dictionary
    employees[name] = salary
    # ask user if they want to enter another employee
    another = input("Do you want to enter another employee? (yes/no): ")
    # if user enters 'no', break the loop
    if another == 'no':
        break

