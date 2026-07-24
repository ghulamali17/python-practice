# Level 1 — Basics (1–20)
# Print "Hello World".
# Print your name, age, and country.
# Take a user's name and greet them.
# Take two numbers and print their sum.
# Calculate the area of a rectangle.
# Calculate the area of a circle.
# Convert Celsius to Fahrenheit.
# Swap two variables.
# Find the square and cube of a number.
# Check whether a number is even or odd.
# Check if a number is positive, negative, or zero.
# Find the largest of two numbers.
# Find the largest of three numbers.
# Check if a year is a leap year.
# Calculate a student's grade.
# Calculate simple interest.
# Convert minutes into hours.
# Convert kilometers to miles.
# Reverse a 3-digit number.
# Calculate the average of five numbers.
import math

# Take a user's name and greet them.
name = input("Enter Your Name: ")
print("Hello", name)

# Take two numbers and print their sum
number1 = int(input("Enter Number 1: "))
number2 = int(input("Enter Number 2: "))
print(number1+number2)

#  Calculate the area of a rectangle
length = int(input("Enter length: "))
width = int(input("Enter width: "))
print("Area:", length * width)

# Calculate the area of a circle.

radius = float(input("Enter Radius: "))
print("Area of circle is", math.pi * radius ** 2)

# Convert Celsius to Fahrenheit.
celsius = float(input("Enter Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", fahrenheit)

#  Swap two variables
a = 5
b = 10

a, b = b, a

print(a, b)

# Find the square and cube of a number


def number(a):
    print("Square:", a ** 2, "Cube:", a ** 3)


number(2)

# Check whether a number is even or odd.


def evenOdd(a):
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")


evenOdd(19)

# Check if a number is positive, negative, or zero


def checkNumber(a):
    if a > 0:
        print("Positive")
    elif a < 0:
        print("Negative")
    else:
        print("Zero")


checkNumber(9)

# Find the largest of two numbers
numbers = [1, 100]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
print(largest)

#  Find the largest of three numbers
numbers = [1, 100, 1000]

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i
print(largest)

# Check if a year is a leap year.


def year(a):
    if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")


year(2000)

# Calculate a student's grade.


def grade(a):
    if a >= 75:
        print("A")
    elif a >= 68:
        print("B")
    elif a >= 62:
        print("C")
    elif a >= 50:
        print("D")
    else:
        print("Fail")


grade(20)

# Calculate simple interest.
amount = int(input("Enter amount: "))
rate = int(input("Enter Rate %: "))
time = int(input("Enter Time (years): "))


interest = (amount * rate * time)/100
print(interest)

# Convert minutes into hours.


def minutes_to_hours(minutes):
    return minutes / 60


print(minutes_to_hours(120))

# Convert kilometers to miles


def kilometers_to_miles(km):
    return km * 0.621371


print(round(kilometers_to_miles(1.6), 2))

# Reverse a 3-digit number

num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))


# Calculate the average of five numbers
def average(a, b, c, d, e):
    return (a+b+c+d+e)/5


print(average(5, 5, 5, 5, 5))
