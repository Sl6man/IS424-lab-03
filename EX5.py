# Write your decorator here
def repeat_hello(x):
    def wrapper():
        for i in range(x):
            hello()
    return wrapper

def hello():
    print('Hello')

x = int(input("Enter a number of repetitions: "))

@repeat_hello(x)
def hello():
    print('Hello')

hello()
