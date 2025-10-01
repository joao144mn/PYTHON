start_campos = True
campo = 1

while start_campos:
    match campo:
        case 1:

            try:
                Nome = str(input("Digite seu nome: "))
                campo += 1
            except:
                print("Valor inválido")

        case 2:
            try:
                Peso = float(input("Digite seu peso em kilos: "))
                campo += 1
            except:
                print("Valor inválido...")

        case 3:
            try:
                Altura = float(input("Digite seu altura: "))
                campo += 1
            except:
                print("Valor inválido...")

        case 4:
            try:
                Idade = int(input("Digite sua idade: "))
                start_campos = False
            except:
                print("Valor inválido...")

IMC = Peso / Altura ** 2 
IMC_arredondado = round(IMC, 2)

print("------DEVOLUÇÃO DE DADOS------")
print("Seu nome completo é ", Nome)
print("seu peso em kilos é ", Peso)
print("Sua altura em metros é ", Altura)
print("Sua idade é ", Idade)
print("Seu IMC é ", IMC_arredondado)



if 20 >= Idade <= 60:
    if IMC < 18.5:
        print("Abaixo do peso")
    elif IMC <= 24.99:
        print("Normal")
    elif IMC <= 29.99:
        print("Sobrepeso")
    else:
        print("Obesidade")

    

if Idade > 60:
    if IMC < 22:
        print("Abaixo do peso")
    elif IMC <= 27:
        print("Normal")
    elif IMC <= 29.99:
        print("Sobrepeso")
    else:
        print("Obesidade")