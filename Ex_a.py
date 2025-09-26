#a) Criar um programa em Python onde o usuário irá digitar seu nome completo, idade e
# peso e ao final deverá mostrar os dados de forma personalizada
# considere se o usuário tiver uma idade menor a 12 anos, mostre que ele é uma criança.
# se ele estiver entre 12 a 18 demonstre que ele é adolescente
# Caso seja acima de 17 a abaixo de 64 anos diga que ele é adulto
# se ele tiver acima de 65 anos diga que ele é aposentado

###operadores lógicos
# >  =  Maior que
# <  =  Menor que
# ==  =  Igual que
# !=  =  Diferente que

# Operadores Aritiméticos
# +  =  Adição
# -  = Subtração
# /  = Divição
# *  = Multiplicação
# ** = Potencia


### Receber os dados
# receber o nome 
nome = input ("Digite seu nome completo: ")
# receber a idade
idade = int(input("Digite sua idade: "))
# receber o peso
peso = int(input("Digite seu peso em Kg: "))
### Processar os dados

# Se a idade for menor que 12 anos, então mostre criança
# Se a idade for maior que 11 anos e menor que 18, então mostre adolescente
# Se a idade for maior que 17 anos e menor que 65 anos, então mostre adolescente
# Se a idade for maior que 64 anos, então mostre aposentado
if idade < 12:
    status = "Criança"
elif idade < 18:
    status = "Adolescente"
elif idade < 65:
    status = "Adulto"
else:
    status = "aposentado"


### Devolver os dados
# devolver nome
print ("Seu nome completo é", nome)
# devolver idade
print("Sua idade é", idade, "anos")
# devolver peso
print ("Seu peso é", peso,"kilos")
# devolver o status
print ("O usuário é um ", status)