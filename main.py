# 1
X = input("Enter number for X")
Y = input("Enter Number for Y")

if X > Y:
    print("if X is bigger than Y")
elif X < Y:
    print("X is smaller than Y")
else:
    print("X equals Y")

# 2
for i in range(0, 5):
    print(i)

# 3
x = range(1, 5)
for i in x:
    if i == 1:
        print("summer")
    elif i == 2:
        print("winter")
    elif i == 3:
        print("fall")
    elif i == 4:
        print("spring")

## 4
# Run 10 times
# 10 will be printed last

# 5
age = 34
first_letterOmMyLastName = "G"
Currency = 3.5
flyAbroad = True
apartment = 14
print(age, first_letterOmMyLastName, Currency, flyAbroad, apartment)
print(age + Currency)

# 6
phoneNum = input("What is your phone number?")
print("phone number is " + phoneNum)


# 7
def print_hello():
    print("Hello")


def calculate():
    print(5 + 3.2)


# 8

def printMyName():
    name = input("Name Please")
    print(name)


def divide(num):
    print(num / 2)


# 9

def returnSum(x, y):
    return x + y


def addSpace99(a, b):
    return a + " " + b


# 10
for i in range(1, 6):
    if i > 1:
        print(end='\n')
    for j in range(1, i + 1):
        print("*", end="")

# 11
for i in range(1, 8):
    if i > 1:
        print(end='\n')
    for j in range(1, 8):
        if j == i:
            print("*", end="")
        elif j == (8 - i):
            print("*", end="")
        else:
            print(" ", end="")


# 12
def getNum():
    num = input("Please enter a number")
    if not num.isnumeric():
        raise Exception("Sorry, this is not a number ")
    return num

sumOfDigits = 0
for i in getNum():
    sumOfDigits = sumOfDigits + int(i)
print("sum of all digits is: ", sumOfDigits)
