numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
if numero1 >= numero2 or numero1 >= numero3:
    print(f'O Maior deles é o : {numero1}')
elif numero2 >= numero3 and numero2 >= numero1:
    print(f'O Maior deles é o : {numero2}')
else: 
    print(f'O Maior deles é o : {numero3}')    
