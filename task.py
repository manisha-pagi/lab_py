#1. Calculate simple interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest is:", simple_interest)
#2. Find maximum of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Maximum number is:", a)
else:
    print("Maximum number is:", b)
#3.print numbers 1to5    
for i in range(1, 6):
    print(i)
#4.Program to find the length of a string
text = "Hello Python"
print("Length of the string is:", len(text))
#5.print a welcome message
print("Welcome to Python programming!")
#6. Print the first character
text = input("Enter a string: ")
print("First character:", text[0])
#7.print last charcter of negative numbers
num = input("Enter a negative number: ")
print("Last digit is:", num[-1])
#8.check positive or negative numbers
# Get input from the user
num = float(input("Enter a number: "))
if num > 0:
    print("The number is Positive")
elif num == 0:
    print("The number is Zero")
else:
    print("The number is Negative")
#9.add three numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
total = num1 + num2 + num3
print("The sum of three numbers is:", total)
#10.take ainput from user
name = input("What is your name? ")
print("Hello, " + name + "!")