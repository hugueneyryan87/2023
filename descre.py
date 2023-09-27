numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 >= numero2 or numero1  >= numero3:
    if numero2 >= numero3:
        print(numero1, numero2, numero3)
    else:
        print(numero1, numero3, numero2)
elif numero2 <= numero3:
    print(numero2, numero3, numero1)
else:
    print(numero3, numero2, numero1)
