opcao = None  # Inicialize a opção com um valor diferente de 0 para entrar no loop

while opcao != 0:
    print('[1] - Cadastrar')
    print('[2] - Excluir')
    print('[3] - Pesquisar')
    print('[0] - Sair')
    
    opcao = int(input('Digite uma opção: '))
    
    if opcao == 1:
        print('[1] - Cadastrar')
    elif opcao == 2:
        print('[2] - Excluir')
    elif opcao == 3:
        print('[3] - Pesquisar')
    elif opcao == 0:
        print('[0] - Sair')
    else:
        print('Opção inválida. Tente novamente.')

print('Programa encerrado.')

