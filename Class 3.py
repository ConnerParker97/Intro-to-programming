var1 = 20
var2 = 13
var3 = 8

if (var1 > var2):
    print ('This is the value of Var1:', var1)

print ('This is the value of Var2:', var2)
print ('This is the value of Var3:', var3)

### Exercise 1
    # Check if var1 is greater than var 2, is so, print 'Var1 is greater than Var2'
if var1 > var2:
    print('Var1 is greater than Var2')
else:
    print('Var1 is not greater than Var2')

### Exercise 2
   # Num1 = 10, write code to test is num1 is even, if so, print yes and the result.

num1 = 10

if num1 % 2 == 0:
    print("Yes, num1 is even.")
else:
    print("No, num1 is not even.")

### Exercise 3
    # input a number, see if it is dividable by 7. if it is not, then print its value. else, print its square.

num = int(input("Enter a number: "))

if num % 7 == 0:
    print("The square of the number is:", num * num)
else:
    print("The number is not divisible by 7. Its value is:", num)

### Exercise 4

# Prompt the user to input a number and convert it to an integer
number = int(input("Enter an integer: "))

# Determine if the number is even or odd
if number % 2 == 0:
    print(f"The number is even.")
else:
    print(f"The number is odd.")


# Exercise 4

# Inputs for the three numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")

# Using nested if-else to find the greatest number
if num1 >= num2:
    if num1 >= num3:
        print("The greatest number is {num1}")
    else:
        print("The greatest number is {num3}")
else:
    if num2 >= num3:
        print("The greatest number is {num2}")
    else:
        print("The greatest number is {num3}")
