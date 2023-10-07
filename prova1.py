PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para:       preti.joao@ifmt.edu.br
Assunto:    Prova 1 de Laboratório de Programação 2023/2
Mensagem:   NOME COMPLETO DO ESTUDANTE
Anexo:      prova1.py
'''
#1. Faça um programa que leia o valor unitário de um produto,
#   a quantidade desejada e imprima o valor total a pagar. (2,5pt)
valor = float(input('Digite O valor do Produto: '))
quantidade = int(input('Quantos desse produto Você Quer: '))
total = valor * quantidade
print(f'Voce Pagara R$ {total}')

#2. Faça um programa que leia 3 números e imprima o maior deles. (2,5pt)
nu1 = int(input('Digite o primeiro numero: '))
nu2 = int(input('Digite o segundo numero: '))
nu3 = int(input('Digite o terceiro numero: '))
if nu1 > nu2 and nu1 > nu3:
    print({nu1}, {nu2}, {nu3})
if nu2 > nu1 and nu2 > nu3:
    print({nu2}, {nu1}, {nu3})
if nu3 > nu1 and nu3 > nu2:
    print({nu3}, {nu2}, {nu1})
        
#3. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#   da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#   a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#   "Reprovado" ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#   reprovação e as demais em prova final). (2,5pt)
nome = str(input('Digite O nome do aluno: '))
nota1 = float(input('Digite nota 1: '))
nota2 = float(input('Digite nota 2: '))
media = (nota1+nota2)/2
if media >= 7:
    print(f'Aluno Aprovado: {media}')
elif media <=3:
    print('Reprovado')
else:
    print('Prova Final: ') 


#4. Faça um programa que apresente um menu com 4 opções:
#   [1] - Cadastrar
#   [2] - Excluir
#   [3] - Pesquisar
#   [0] - Sair
#   O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
#   ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
#   escolhida for zero (0). (2,5pt)
print('Dgite Uma das Opção: ')
print('[1] - Cadastrar')
print('[2] - Excluir')
print('[3] - Pesquisar')
print('[0] - Sair')
opcao = ''
#opcao = int(input('Cadastro Digite Uma as Opção:'))
while opcao !=0:
    opcao = int(input('Cadastro Digite Uma as Opção:'))    
    if opcao == 1:
        print('[1] - Casdastrar')
    elif opcao == 2:
        print('[2] - Excluir')
    elif opcao == 3 :
        print('[3] - Pesquisar')
    elif opcao == 0:
        print ('[4] - Sair ')