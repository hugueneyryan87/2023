numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

maior = numero1

if numero2 > maior or numero3 > maior:
    if numero2 > numero3:
        maior = numero2
    else:
        maior = numero3

print("O maior número é:", maior)
