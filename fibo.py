#9. No dia da estréia do filme "Procurando Dory", uma grande emissora de TV realizou
#uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
#a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
#opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam excelente;
#• A quantidade de pessoas que responderam regular;
#• A percentagem de pessoas que responderam bom entre todos os expectadores
#analisados. 
cont = 1
soma_idade=0
cont_regular=0
cont_bom=0
while cont <= 5:
    idade = int(input('Digite a IDADE: '))
    print('Dê Sua Avaliação Sobre o Filme: ')
    print('1 Para EXCELENTE:')
    print('2 Para BOM: ')
    print('3 Para REGULAR: ')
    cont+=1
    nota = int(input('NOTA :>> '))
    if nota == 0 or nota >3:
        print('NOTA INVALIDA:')
        break
    if nota == 1:
        soma_idade = idade + soma_idade
    if nota == 3:
        cont_regular+=1
    if nota == 2:
        cont_bom+=1
print(f'A média das idades das pessoas que responderam excelente é de: {soma_idade/5}')
print(f'A quantidade de pessoas que responderam regular foi de: {cont_regular}')
print(f'{(cont_bom*100)/100} % BOM entre todos os expectadores analisados.')




    
    


