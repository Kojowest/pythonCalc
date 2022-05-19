print("Enter 1 to perform ADDITION")
print("Enter 2 to perform SUBTRACTION")
print("Enter 3 to perform DIVISION")
print("Enter 4 to perform MULTIPLICATION")
print("Enter 5 to perform MODULUS")

operation = input()

if(operation == '1'):
    num1 = input('Enter the first number')
    num2 = input('Enter the first number')
    result = (int(num1) + int(num2))
    print(result)
elif(operation == '2'):
    num1 = input('Enter the first number')
    num2 = input('Enter the first number')
    result = (int(num1) - int(num2))
    print(result)
elif(operation == '3'):
    num1 = input('Enter the first number')
    num2 = input('Enter the first number')
    if(int(num2) == 0):
        print('Denominator cannot be zero')
    else:
        result = (int(num1) / int(num2))
        print(result)
elif(operation == '4'):
    num1 = input('Enter the first number')
    num2 = input('Enter the first number')
    result = (int(num1) * int(num2))
    print(result)
elif(operation == '5'):
    num1 = input('Enter the first number')
    num2 = input('Enter the first number')
    if(int(num2) == 0):
        print('Denominator cannot be zero')
    else:
        result = (int(num1) / int(num2))
        print(result)





