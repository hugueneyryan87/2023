# Ler três números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

# Encontrar o menor, o meio e o maior valor
if numero1 <= numero2 and numero1 <= numero3:
    menor = numero1
    if numero2 <= numero3:
        meio = numero2
        maior = numero3
    else:
        meio = numero3
        maior = numero2
elif numero2 <= numero1 and numero2 <= numero3:
    menor = numero2
    if numero1 <= numero3:
        meio = numero1
        maior = numero3
    else:
        meio = numero3
        maior = numero1
else:
    menor = numero3
    if numero1 <= numero2:
        meio = numero1
        maior = numero2
    else:
        meio = numero2
        maior = numero1

# Imprimir os números em ordem crescente
print("Números em ordem crescente:", menor, meio, maior)
