#4. Faça um programa que apresente um menu com 4 opções:
#   [1] - Cadastrar
#   [2] - Excluir
#   [3] - Pesquisar
#   [0] - Sair
#   O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
#   ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
#   escolhida for zero (0). (2,5pt)
opcao = ''
while opcao !=0:
    print('Escolha uma opção: ') 
    print('[1] - Cadastrar')
    print('[2] - Excluir')
    print('[3] - Pesquisar')
    print('[0] - Sair')
    opcao = int(input('Digite Uma as Opção:'))
    if opcao == 1:
        print('[1] - Casdastrar')
    if opcao == 2:
        print('[2] - Excluir')
    if opcao == 3 :
        print('[3] - Pesquisar')
    if opcao == 0:
        print ('[4] - Sair ')