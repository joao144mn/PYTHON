#Crie uma calculadora com as 4 operações matemáticas (Multiplicação, Soma,
#Subtração e Divisão);

### ------ RECEBER
# receber o numero 1
num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
# receber a operação
print("\n----INFORME UMA OPERAÇÃO----\n")
print("Digite X para multiplicar")
print("Digite / para dividir")
print("Digite + para somar")
print("Digite - para subtrair\n")
oper = input("Informe a operação: ")
# receber o numero 2


### ----- PROCESSAR

if oper == "X" or oper == "x":
    resultado = num1 * num2
elif oper == "-":
    resultado = num1 - num2
elif oper == "/":
    resultado = num1 / num2
elif oper == "+":
    resultado = num1 + num2
else:
    resultado = "INEXISTENTE"

print("O resultado é: ", resultado)