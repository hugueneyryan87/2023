cont = 1
while cont <= 5:
    idade = int(input('Digite a IDADE: '))
    print('Dê Sua Avaliação Sobre o Filme: ')
    print('1 Para Excelente:')
    print('2 Para Bom: ')
    print('3 Regular: ')
        #total_idade +=idade
        #media = total_idade/5
    nota = int(input('NOTA :>> '))
    if nota == 0 or nota >3:
        print('NOTA INVALIDA:')
        break
    excelente =0
    bom =0
    regular =0
    media_excelente = 0
    media_bom = 0 
    media_regular = 0
    idade_mediaE=0
    idade_bom =0
    idade_regular =0
    pessoa_excelente=0 
    pessoa_bom =0 
    total_porcentagem =0
    soma_idade=0
    if nota == 1:
        excelente +=1
        media_excelente +=1
        idade_mediaE = idade
        pessoa_excelente +=1
    elif nota == 2:
        bom +=1
        media_bom +=1
        idade_bom = idade
        soma_bom = idade_bom+soma_bom
        pessoa_bom +=1
    elif nota == 3:
        regular +=1
        media_regular +=1 
        idade_regular = idade
        soma_regular = idade + soma_idade
        pessoa_regular +=1
        total_porcentagem=(bom-(regular+excelente)/100)
        print(f'A média das idades das pessoas que responderam excelente: {media/5}') 
        print(f'A quantidade de pessoas que responderam regular: {pessoa_regular}')  
        print(f'Porcentagem de pessoas que responderam BOM entre todos os expectadores Analisados:')