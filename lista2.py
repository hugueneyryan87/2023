'''
Exercícios sobre os comandos de condição em python
'''

from datetime import date, datetime

TODAY = datetime.now()

def exemploSe():
    n1 = float(input('Nota1: '))
    n2 = float(input('Nota2: '))
    media = (n1 + n2) / 2
    if media >= 6:                  #SE
        print('APROVADO!!!')
    else:                           #SENAO
        pf = float(input('Nota da PF: '))
        media = (media + pf) / 2
        if media >= 5:
            print('APROVADO NA PF!!!')
        else:
            print('REPROVADO!!!')

def exemploSe2():
    opcao = int(input('Opção: '))
    if opcao == 0:
        print('Escolheu 0')


    elif opcao == 1:
        print('Escolheu 1')
    elif opcao == 2:
        print('Escolheu 2')
    elif opcao == 3:
        print('Escolheu 3')    
    else:
        print('Opção Inválida!')
        
#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.
def q01():
    numero1 = int(input('Digite um Valor:'))
    numero2 = int(input('Digite Outro Valor:'))
    resultado = numero1 + numero2
    if resultado > 10:
        print(resultado)
    else:
        print(f'Numero menor que 10: {resultado}')

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.
def q02():
    numero1 = int(input('Digite um Valor:'))
    numero2 = int(input('Digite Outro Valor:'))
    resultado = numero1 + numero2
    if resultado > 20:
        print(f'O numero é maior que 20 >>: {resultado+8}')
    else:    
        print(f'O numero é menor que 20 <<: {resultado-5}')
       
    #3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q03():
    numero = int(input('Entre com um valor inteiro : '))
    if numero % 3==0: 
        print(f'{numero} É Multiplo de 3 :')
    else:
        print(f'{numero} Não é Multiplo de 3 :')

    #4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.
def q04():
    numero = int(input('Digite um numero Idiota, kkk : '))
    if numero % 5 ==0:
        print(f'{numero} é divisivel por 5 :')
    else:
        print(f'{numero} Não divisivel por 5 :')    
    

#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.
def q05():
    numero = int(input('Digite um numero: '))
    if (numero % 3 ==0) and (numero % 7 ==0):
        print(f'{numero}, é Divisivel por 3 e 7 :')
    else:
        print('Nao é divisivel :')        

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
def q06():
    salario = float(input('Digite o Salario do Funcionario : '))
    prestacao = float(input('Digite o Valor da prestação : '))
    if prestacao <= salario *0.30:
        print('Emprestimo concedido :')
    else:
        print('Emprestimo Não Concedido: ')
#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.
def q07():
    numero = int(input('Digite um Numero :'))
    if (numero >=20) and (numero <= 50):
        print('O numero esta entre 20 e 50 :')
    else:
        print(f'o Numero {numero} Não esta entre 20 e 50:')     

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".
def q08():
    numero = int(input('Digite um Valor Otario :'))
    if numero > 20:
        print('O numero é Maior que 20 : ')
    elif numero ==20:
        print('Numero Igual a 20 :')
    else:
        print('Numero Menor do que 20 :')


#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.
def q09():
    ano_nascimento = int(input('Digite um Ano de Nascimento: '))
    if ano_nascimento <1910:
        print('Ano invalido!!!!!!!!: ')
    else:
        anoatual = int(input('Digite o ANO atual: '))
        idade = anoatual-ano_nascimento
        print(f'Voce tem {idade} anos de idade: ')

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.
def q10():
    numero1 = int(input('Digite o Primeiro Numero: '))
    numero2 = int(input('Digite um segundo Numero: '))
    numero3 = int(input('Digite um Terceiro numero: '))
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
    print("Números em ordem crescente:", menor, meio, maior)




#11. Faça um programa que leia 3 números e imprima o maior deles.
def q11():
    numero1 = float(input('Digite Um numero: '))
    numero2 = float(input('Digite um segundo Numero: '))
    numero3 = float(input('Digite um terceiro Numero: '))
    if numero1 >= numero2 and numero1 >= numero3:
        maior = numero1
    elif numero2 >= numero1 and numero2 >=numero3:
        maior = numero2
    else:
        maior = numero3
        print('O Maior deles é o ', maior)       
#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idadea
#• Se é maior de 65 anos
def q12():
    idade = int(input('Digite sua idade: '))
    if (idade >= 18)and(idade<=64):
        print('Voce é maior de idade: ')
    elif idade < 18:
        print('Voce é Menor de idade: ')
    elif idade >=65:
        print('Voce é maior que 65 Anos:')        
#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).
def q13():
    
    nome = str(input('Digite um nome: '))
    nota1 = float(input('Digite a nota da prova :'))
    nota2 = float(input('Digite a nota da segunda prova: '))
    media = (nota1+nota2)/2
    print(f'O aluno {nome}, primeira nota {nota1} e segunda {nota2} da prova, com media de {media}')
    if media >= 7:
        print('APROVADO!!!!')
    elif media <7:
        print(f'Aluno {nome} Foi para PF: ')
        pf = float(input('Digite a nota da Prova final: '))
        mediafinal = (pf+nota1+nota2)/3
    if media > 3:    
        print(f'APROVADO Na PF COM MEDIA :{media} ')
    else:
        print(f'REPROVADO na PF: {media}')            
    
    

#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%
def q14():
    salario = float(input('Digite o Salario da Pessoal: '))
    if salario <= 600:
        print('Você Esta Isento: ')
    elif salario > 600 and salario <= 1200:
        print(f'Com desconto de 20 % , fica: {(salario-(salario*0.20))}')    
    elif salario > 1200 and salario <= 2000:
        print(f'Com desconto 25 % , fica: {(salario-(salario*0.25))}')
    elif salario >2000:
        print(f'Com desconto 30 %, fica: {(salario-(salario*0.30))}')

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.
def q15():
    produto = float(input('Digite o Valor TOTAL DA COMPRA: '))
    if produto < 20:
        print(f'A COMPRA tera 45% de lucro: {(produto+(produto*0.45))}')
    else:
        print(f'A COMPRA tera 30% de lucro: {(produto+(produto*0.30))}')    


#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos
def q16():
    print('BEM VINDO AO CAMPEONATO DE NATAÇÃO:')
    idade = int(input('Digite a Idade do Participante: '))
    if idade >=5 and idade <=7:
        print(f'O Participante será na categoria INFANTIL A: {idade}')
    elif idade >=8 and idade <=10:
        print(f'O Participante Será na categoria INFANTIL B:{idade}')
    elif idade >=11 and idade <=13:
        print(f'O Participante Será na categoria JUVENIL A:{idade}')
    elif idade >=14 and idade <=17:
        print(f'O Participante será na categoria JUVENIL B:{idade}')  
    else : 
        idade >= 18
        print(f'Categoria Sênior: {idade}')             
    

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00
def q16():
    nome = str(input('Digite um nome: '))
    idade = int(input('Digite a idade: '))
    if idade <= 10:
        print(f'O usuario {nome}, Com a idade de {idade} Anos, Vai pagar R$ 30 no Plano de Saude: ')
    elif idade >10 and idade <= 29:
        print(f'O usuario {nome}, Com a idade de {idade} Anos, Vai pagar R$ 60 no Plano de Saude: ')
    elif idade >29 and idade <= 45:
        print(f'O usuario {nome}, Com a idade de {idade} Anos, Vai pagar R$ 120 no Plano de Saude: ') 
    elif idade >45 and idade <=59:
        print(f'O usuario {nome}, Com a idade de {idade} Anos, Vai pagar R$ 150 no Plano de Saude: ')
    elif idade >59 and idade <=65:
        print(f'O usuario {nome}, Com a idade de {idade} Anos, Vai pagar R$ 250 no Plano de Saude: ') 
    elif idade > 65:
        print(f'O usuario {nome}, Com a idade de {idade} Anos, Vai pagar R$ 400 no Plano de Saude: ')              

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.
def q18():
    mes = int(input('Digite um numero para Mês: '))
    if mes == 0 or mes >=13:
        print('NÂO EXISTE UM MES PARA ESSE NUMERO:')
    if mes == 1:
        print('Voce escolheu Janeiro:')
    elif mes ==2:
        print('Voce escolhe Fevereiro:')        
    elif mes ==3:
        print('Voce escolhe Março:')
    elif mes ==4:
        print('Voce escolhe Abril:')
    elif mes ==5:
        print('Voce escolhe Maio:')
    elif mes ==6:
        print('Voce escolhe Junho:')
    elif mes ==7:
        print('Voce escolhe Julho:')
    elif mes ==8:
        print('Voce escolhe Agosto:')
    elif mes ==9:
        print('Voce escolhe Setembro:')
    elif mes ==10:
        print('Voce escolhe Outubro:')
    elif mes ==11:
        print('Voce escolhe Novembro:')
    elif mes ==12:
        print('Voce escolhe Dezembro:')                                    
#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses valores em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".
def q19():
    #estado = str(input('De qual estado é essa equipe:'))
    jogadorA = float(input('Digite o Pontos do Jogador A:'))
    jogadorB = float(input('Digite o Pontos do Jogador B:'))
    jogadorC = float(input('Digite o Pontos do Jogador C:'))
    maior = jogadorA
    if jogadorB > maior or jogadorC > maior:
        if jogadorB > jogadorC:
            maior = jogadorB
        else: 
            maior = jogadorC
    
    pass
#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio
def q20():
    saldo = float(input("DIGITE SEU SALDO!!!!: "))
    if saldo >=0 and saldo <= 500:
        print("!!!NENHUM CREDITO!!!")
    elif saldo >= 501 and saldo <= 1000:
        print(f'Com Saldo de R$={saldo}, Voce terá Saldo medio de 30%: ')
    elif saldo >= 1001 and saldo <= 3000:
        print(f'Com Saldo de R$={saldo}, Voce terá Saldo medio de 40%: ')
    elif saldo > 3001 :
        print(f'Com Saldo de R$={saldo}, Voce terá Saldo medio de 50%: ')


#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:
def q21():
    nomelivro = str(input('Digite o nome do Livro: '))
    print('Voce é Professor ou Aluno: ')
    print('Digite 1 Para Professor: ')
    print('Digite 2 Para Aluno: ')
    opcao = int(input('Digite a Opção: '))
    if opcao == 1:
        print('Você Professor')
        print(f"O Livro, {nomelivro}, Você tem 10 dias Para entregar o Livro: ")
    elif opcao == 2:
        print('Você Aluno')
        print(f"O Livro, {nomelivro}, Você tem 3 dias Para entregar o Livro: ")  
    else:
        print('Opção IVALIDA!!!!!')  

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.
def q22():
    km = int(input("Digite o KM a Percorrer: "))
    tipo = str(input('Digite o Tipo do Veiculo: '))
    if tipo == 'a' :
        print(f'O Carro tipo A, vai consumir {km/12}, para percorrer {km} Km: ')
    elif tipo == 'b' :
        print(f'O Carro tipo B, vai consumir {km/9}, para percorrer {km} Km: ')
    elif tipo == 'c' : 
        print(f'O Carro tipo C, vai consumir {km/8}, para percorrer {km} Km: ')    

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano 180cal Abacaxi 75cal   Chá 20cal
#Peixe 230cal   Sorvete diet 110cal Suco de laranja 70cal
#Frango 250cal  Mousse diet 170cal  Suco de melão 100cal
#Carne 350cal   Mousse chocolate 200cal Refrigerante diet 65cal
def q23():
    print('Escolha Um Prato: ')
    print('--peixe--frango--carne--')
    opcao = str(input('Digite Nome do prato Acima: '))
    if opcao == 'peixe':
        caloria = 230
    elif opcao == 'frango':
        caloria = 250
    elif opcao == 'carne':
        caloria = 350
    
    print('--sorvete diet--mousse diet-- mousse chocolate--')
    mesa = str(input('Digite opção de Sobremesa Acima: '))
    if mesa == 'sorvete diet':
        y = 100
    elif mesa == 'mousse diet':
        y = 170
    elif mesa == 'mousse chocolate':
        y = 200 
    
    print('--laranja--melao-- refrigerante--')
    suco = str(input('Qual suco Acima deseja: '))
    if suco == 'laranja':
        s = 70
    elif suco =='melao':
        s = 100
    elif suco == 'refrigerante':  
        s = 65
    print(f'Voce Consumira, {y+s+caloria} Calorias')                           


#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos

opcao = int(input('Digite o número da questão: '))
match opcao:
    case 1: q01()
    case 2: q02()
    case 3: q03()
    case 4: q04()
    case 5: q05()
    case 6: q06()
    case 7: q07()
    case 8: q08()
    case 9: q09()
    case 10: q10()
    case 11: q11()
    case 12: q12()
    case 13: q13()
    case 14: q14()
    case 15: q15()
    case 16: q16()
    case 17: q17()
    case 18: q18()
    case 20: q20()
    case 21: q21()
    case 22: q22()
    case 23: q23()


        