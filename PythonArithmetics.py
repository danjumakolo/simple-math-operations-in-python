# Python program to perform basic arithmetic operations

# Take user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
if num2 != 0:
    quotient = num1 / num2
else:
    quotient = "Undefined (cannot divide by zero)"

# Display results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
