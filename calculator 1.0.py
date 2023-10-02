operator = input("Coloque um operador (+ - * /): ")
num1 = float(input("Coloque o primeiro número:"))
num2 = float(input("Coloque o segundo número:"))

if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
    result = num1 / num2
    print(round(result,3))
else:
    print(f"{operator} não é um operador válido")