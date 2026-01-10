#1.Print Message
print("Hello,World!")
print("welcome to python programming")
#2.Add Two Numbers
a=20
b=30
print(a+b)
#3.Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
#4. Check Leap Year
year = int(input("Enter a year: "))

if (year % 400 == 0):
    print(f"{year} is a leap year.")
elif (year % 100 == 0):
    print(f"{year} is not a leap year.")
elif (year % 4 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.") 
#5. Print  PI Vale
import math

radius = 5
area = math.pi * (radius ** 2)

print(f"The area of the circle is: {area:.2f}") 
#6.Store And Print Constant vlue      
PI = 3.14159
GRAVITY = 9.8
DATABASE_URL = "https://api.example.com/v1"
#7.Square of a Number
num = 5
square = num ** 2

print(f"The square of {num} is {square}")
#8. Area Of Circle
import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)
r = 7
print(f"Area: {calculate_circle_area(r)}")
#9.Check Data Type
x = 10          # Integer
y = 10.5        # Float
z = "Hello"     # String
a = [1, 2, 3]   # List

print(type(x))  
print(type(y))  
print(type(z))  
print(type(a))  
#10.Use Math Functions
import math

print(math.ceil(4.1))   # Output: 5
print(math.floor(4.9))  # Output: 4
#11.Find Power
# pow(base, exponent)
print(pow(2, 3))  # Output: 8
#12.Check Positive or Nagative
num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")


