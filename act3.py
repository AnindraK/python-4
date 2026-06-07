def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

print("Sum:",num1, "+", num2, "=", add(num1,num2))
print("difference:",num1, "-", num2, "=", subtract(num1,num2))
print("Product:",num1, "*", num2, "=", multiply(num1,num2))
print("Quotient:",num1, "/", num2, "=", divide(num1,num2))