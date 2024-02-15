# Create a variable to store the number
number = int(input("Enter a number: "))

# loop through the range of 1 to 11

for i in range(1, 11):
    # multiply the number by the current value of i
    result = number * i
    # display the result
    print(f"{number} x {i} = {result}")

