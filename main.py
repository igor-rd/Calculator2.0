a = float(input("Введите число1"))
operation = input('Знак "+, -, *, /"')
b = float(input("Введите число2"))
result = 0



if operation == "+":
    result = a+b
elif operation == "-":
    result = a-b
elif operation == "*":
    result = a*b
elif operation == "/":
    result = a / b

print (f"Результат: {result}")