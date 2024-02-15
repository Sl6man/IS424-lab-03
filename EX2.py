
# Create an empty list
numbers = []

# ask user to input 10 values into the list
for i in range(10):
    # input a number
    number = int(input("Enter a number: "))
    # add the number to the list
    numbers.append(number)


# set the first number in the list as the largest number
largest = numbers[0]

# loop through the list
for number in numbers:
    # if the number is greater than the largest number
    if number > largest:
        # set the number as the largest number
        largest = number

# display the largest number
print("The largest number is:", largest)
