'''
Lista de Exercícios referentes a estruturas de iteração (repetição)


'''


#1.Faça um programa que imprima todos os números de 1 até 100.
def q01():
    for x in range(1,101):
        print(x)
        #2. Faça um programa que imprima todos os números pares de 100 até 1.
def q02():
    for x in range(2,101,2):
        print(x)
#3. Faça um programa que imprima os múltiplos de 5, no intervalo de 1 até 500.
def q03():
    x=1
    while x < 501:
        if x % 5==0:
            print(x)
#4. Faça umprograma que permita entrar com o nome, a idade e o sexo de 20
#pessoas.O programa deve imprimir o nome da pessoa se ela for do sexo masculino
#e tiver mais de 21 anos.
def q04():
    x=1
    while x <= 20:
        print(f'CADASTRO -',x)
        nome = str(input('Digite UM NOME, Ou Digite Sair Para encerrar cadastro: '))
        if nome == 'sair':
            break
        idade = int(input('Digite A IDADE: '))
        sexo  = str(input('Digite O SEXO: '))
        x+=1
        if idade > 21 and sexo == 'm' or sexo =='M':
        
            print({nome , idade , sexo})
#5. Sabendo-se que a unidade lógica e aritmética calcula o produto através de somas
#sucessivas, crie um programa que calcule o produto de dois números inteiros
#lidos. Suponha que os números lidos sejam positivos.
def q05():
    anterior=0
    atual=1
    soma=0
    for atual in range(1,6):
        print(soma)
        soma = atual+anterior
        atual+=atual
#6. Crie um programa que imprima os 20 primeiros termos da série de Fibonacci.
#Observação: os dois primeiros termos desta série são 1 e 1 e os demais são gerados
#a partir da soma dos anteriores. Exemplo:
#• 1 + 1 = 2, terceiro termo;
#• 1 + 2 = 3, quarto termo, etc.
def q06():
    anterior=0
    atual=1
    for x in range(20):
        print(atual)
        proximo=anterior+atual
        anterior=atual
        atual=proximo
#7. Crie um programa que permita entrar com o nome, a nota da
#prova 1 e da prova 2 de 15 alunos. Ao final, imprimir uma listagem, contendo:
#nome, nota da prova 1, nota da prova 2, e média das notas de cada aluno. Ao final,
#imprimir a média geral da turma.
def q07():
    cont = 1
    mediageral = 0
    while cont <=3:
        nome = str(input('Digite o Nome do Aluno: '))
        nota1 = float(input('Digite a Primeira Nota: '))
        nota2 = float(input('Digite a Segunda Nota: '))
        cont+=1
        media=(nota1 + nota2)/2
        print(f'{nome}, {nota1}, {nota2}, {media}')
        mediageral = mediageral+media
    print(f'Media da turma{mediageral/3}')
#8. Faça umprograma que permita entrar com o nome e o salário bruto de 10 pessoas.
#Após ler os dados, imprimir o nome e o valor da alíquota do imposto de renda
#calculado conforme a tabela a seguir:
#Salário IRRF
#Salário menor que R$1300,00 Isento
#Salário maior ou igual a R$1300,00 e menor que R$2300,00 10% do salário bruto
#Salário maior ou igual a R$2300,00 15% do salário bruto
def q08():
    cont = 1
    while cont <= 2:
        nome=str(input('Digite um nome: '))
        cont+=1
        if nome == 'Sair':
            break
        salario = float(input('Digite O SALARIO: '))
        if salario <=1300:
            print('<< Isento >>: ')
        elif salario >= 1300 and salario <= 2300:
            total= (salario -(salario - 0.10)/100)
            subtrair = salario - total
            print(f'Com R$ {salario}, {nome}, Menos 10% {salario- ((salario - 0.10)/100):.2f}')
            print(f'Total de {subtrair :.2f} de Desconto do IRRF:')
        elif salario >= 2300:
            total=(salario-(salario - 0.15)/100)
            subtrair = salario - total
            print(f'Com R$ {salario}, {nome}, Menos 15% {salario- ((salario - 0.15)/100):.2f}')
            print(f'Total de {subtrair :.2f} de Desconto do IRRF:')    
#9. No dia da estréia do filme "Procurando Dory", uma grande emissora de TV realizou
#uma pesquisa logo após o encerramento do filme. Cada espectador respondeu
#a um questionário no qual constava sua idade e a sua opinião em relação ao filme:
#excelente - 3; bom - 2; regular - 1. Criar um programa que receba a idade e a
#opinião de 20 espectadores, calcule e imprima:
#• A média das idades das pessoas que responderam excelente;
#• A quantidade de pessoas que responderam regular;
#• A percentagem de pessoas que responderam bom entre todos os expectadores
#analisados.
def q09():
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
#10. Em um campeonato Europeu de Volleyball, se inscreveram 30 países. Sabendo-se
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12
#jogadores, crie um programa que apresente as seguintes informações:
#
#• O peso médio e a idade média de cada um dos paises;
#• O atleta mais pesado de cada time;
#• O atleta mais jovem de cada time;
#• O peso médio e a idade média de todos os participantes.
def questao10():
    pass
    
#11. Construa um programa que leia vários números e informe quantos números
#entre 100 e 200 foram digitados. Quando o valor 0 (zero) for lido, o algoritmo
#deverá cessar sua execução.
def q11():
    cont=0
    numero=''
    while numero !=0:
        numero= int(input('Digite Um numero ou 0 Para parar: '))
        if numero > 100 and numero <200:
            cont+=1
        
    print(f'Voce Digitou {cont} de Numeros entre 100 e 200: ')        

#12. Dado um país A, com 5 milhões de habitantes e uma taxa de natalidade de 3% ao
#ano, e um país B com 7 milhões de habitantes e uma taxa de natalidade de 2% ao
#ano, fazer um programa que calcule e imprima o tempo necessário para que a
#população do país A ultrapasse a população do país B.
def q12():
    paisA =5000000
    paisB =7000000
    ano =0
    while paisA < paisB:
        
        paisA =paisA + paisA * 0.03
        paisB =paisB + paisB * 0.02
        ano+=1
    print(f'Será Preciso {ano} Anos, Para o Pais A {paisA} ser Maior que Pais B: {paisB}')


#13. Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medidores
#de consumo. Para cada consumidor, são digitados os seguintes dados:
#• número do consumidor
#• quantidade de kWh consumidos durante o mês
#• tipo (código) do consumidor
#1-residencial, preço em reais por kWh = 0,3
#2-comercial, preço em reais por kWh = 0,5
#3-industrial, preço em reais por kWh = 0,7
#Os dados devem ser lidos até que seja encontrado o consumidor com número 0
#(zero). O programa deve calcular e imprimir:
#• O custo total para cada consumidor
#• O total de consumo para os três tipos de consumidor
#• Amédia de consumo dos tipos 1 e 2

#14. Faça um programa que leia vários números inteiros e apresente o fatorial de cada
#número. O algoritmo encerra quando se digita um número menor do que 1.n
def q14():
    numero = 0
    seguinte = 0
    atual = 0
    while numero !=0:
        numero = int(input('Digite Varios numeros ou 0 p/ SAIR: '))
        seguinte = numero * seguinte
        print(seguinte)
        atual = seguinte
               
 #anterior=0
  #  atual=1
   # for x in range(20):
    #    print(atual)
     #   proximo=anterior+atual
      #  anterior=atual
       # atual=proximo


#15. Faça um programa que permita entrar com a idade de várias pessoas e
#imprima:
#• total de pessoas com menos de 21 anos
#• total de pessoas com mais de 50 anos
def q15():
    cont_menos=0
    cont_mais=0
    idade = 0
    while idade !=0:
        idade = int(input('Digite Idade, Ou 0 Para SAIR: '))
        if idade ==0:
            break
        if idade < 21:
            cont_menos +=1
        elif idade > 50:
            cont_mais +=1
    print(f'São {cont_menos} Pessoas, com Menos de 21 ANOS:  ')                    
    print(f'São {cont_mais} Pessoas, com Menos de 50 ANOS:  ')


#16. Sabendo-se que a unidade lógica e aritmética calcula a divisão por meio de subtrações
#sucessivas, criar um algoritmo que calcule e imprima o resto da divisão de
#números inteiros lidos. Para isso, basta subtrair o divisor ao dividendo, sucessivamente,
#até que o resultado seja menor do que o divisor. O número de subtrações
#realizadas corresponde ao quociente inteiro e o valor restante da subtração corresponde
#ao resto. Suponha que os números lidos sejam positivos e que o dividendo
#seja maior do que o divisor.
#Exemplo:
#  10 / 5
#  10 é o Dividendo
#  5 é o Divisor
#  2 é o Quociente (resultado inteiro da divisão)
#  0 é o Resto da Divisão
def q16():
    resto =''
    resultado=''
    cont=1
    numero = float(input('Digite um Numero: '))
    divisor = float(input('Digite O dividendo: '))
    resto = numero % divisor
    resultado = numero / divisor
    print(resultado)
    while resultado > resto: 
        resultado = numero / divisor
        resto = numero % divisor

        cont+=1
    print(cont)  
    pass  

    

#17. Crie um programa que possa ler um conjunto de pedidos de compra e
#calcule o valor total da compra. Cada pedido é composto pelos seguintes campos:
#• número de pedido
#• data do pedido (dia, mês, ano)
#• preço unitário
#• quantidade
#O programa deverá processar novos pedidos até que o usuário digite 0 (zero)
#como número do pedido.
def q17():
    pedido = int(input('Numero do pedido: '))

#18. Uma pousada estipulou o preço para a diária em R$30,00 e mais uma taxa de
#serviços diários de:
#• R$15,00, se o número de dias for menor que 10;
#• R$8,00, se o número de dias for maior ou igual a 10;
#Faça umprograma que imprima o nome, a conta e o número da conta de cada
#cliente e ao final o total faturado pela pousada.
#O programa deverá ler novos clientes até que o usuário digite 0 (zero) como
#número da conta.

#19. Emuma Universidade, os alunos das turmas de informática fizeram uma prova
#de algoritmos. Cada turma possui um número de alunos. Criar um programa que
#imprima:
#• quantidade de alunos aprovados;
#• média de cada turma;
#• percentual de reprovados.
#Obs.: Considere aprovado comnota >= 7.0
def q19():
    pass    

#20. Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:
#• Qual o seu time de coração?
#1-Fluminense;
#2-Botafogo;
#3-Vasco;
#4-Palmeiras;
#5-Outros
#• Onde você mora?
#1-RJ;
#2-Niterói;
#3-Outros
#• Qual o seu salário?
#Faça um programa que imprima:
#• o número de torcedores por clube;
#• a média salarial dos torcedores do Botafogo;
#• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
#clubes;
#• o número de pessoas de Niterói torcedoras do Fluminense
#3.12. Exercícios da Aula 73
#Obs.: O programa encerra quando se digita 0 para o time.
def q20():
    cont_flu = 0
    cont_fogo = 0
    cont_vasco = 0
    cont_palme = 0
    cont_rj = 0
    cont_niteroi = 0
    cont_outros = 0
    cont_times_outros = 0
    torcedor_outros = 0
    flu_niteroi = 0
    time = ''
    cidade = ''
    while time == '0':
        time = str(input('Qual o Seu time do Coração: '))
        if time == 'fluminense':
            cont_flu += 1
        if time == 'botafogo':
            cont_fogo += 1
        if time == 'vasco':
            cont_vasco += 1
        if time == 'palmeiras':
            cont_palme += 1
        if time == 'outros':
            cont_times_outros +=1    
        cidade = str(input('Qual cidade Você Mora: Rj , Niteroi , Outros: '))
        if cidade =='rj':
            cont_rj += 1
        if cidade == 'niteroi':
            cont_niteroi += 1
        if cidade == 'outros':
            cont_outros += 1
            salario = float(input('Qual Seu Salario: '))
        if cont_flu >0:
            print(f'{cont_flu} São torcedore do Fluminense: ')
        if cont_fogo >0:
            print(f'{cont_fogo} São tordedores do Botafogo: ')
        if cont_vasco >0:
            print(f'{cont_vasco} São tordedores do Botafogo: ')
        if cont_palme > 0:
            print(f'{cont_palme} São tordedores do Palmeiras: ')
        if time == 'botafogo':
            media_salario = salario / cont_fogo
        if cidade == 'rj' and time == 'outros':
            torcedor_outros +=1
        if time == 'fluminense' and cidade == 'niteroi':    
            flu_niteroi += 1
    print(f'Torcedores do Fluminense {cont_flu}')
    print(f'Torcedores do Botafogo {cont_fogo}')
    print(f'Torcedores do Vasco  {cont_vasco}')
    print(f'Torcedores do Palmeiras {cont_palme}')
    print(f'Torcedores Outros  {cont_times_outros}')
    print(f'A Média Do Salarios dos Botafoguense: {media_salario}')
    print(f'Pessoas que mora no Rio de Janeiro  e Torce para outros Times: {torcedor_outros}')
    print(f'As pessoas que mora em Nitéroi e Torce para o Fluminense: {flu_niteroi}')
#• o número de torcedores por clube;
#• a média salarial dos torcedores do Botafogo;
#• o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
#clubes;
#• o número de pessoas de Niterói torcedoras do Fluminense
#3.12. Exercícios da Aula 73
#Obs.: O programa encerra quando se digita 0 para o time.            

    

    
                    




#21. Emuma universidade cada aluno possui os seguintes dados:
#• Renda pessoal;
#• Renda familiar;
#• Total gasto com alimentação;
#• Total gasto com outras despesas;
#Faça um programa que imprima a porcentagem dos alunos que gasta acima de
#R$200,00 com outras despesas. O número de alunos com renda pessoal maior
#que a renda familiar e a porcentagem gasta com alimentação e outras despesas
#em relação às rendas pessoal e familiar.
#Obs.: O programa encerra quando se digita 0 para a renda pessoal.

#22. Crie um programa que ajude o DETRAN a saber o total de recursos que foram
#arrecadados com a aplicação de multas de trânsito.
#O algoritmo deve ler as seguintes informações para cada motorista:
#• número da carteira de motorista (de 1 a 4327);
#• número demultas;
#• valor de cada uma das multas.
#Deve ser impresso o valor da dívida para cada motorista e ao final da leitura o
#total de recursos arrecadados (somatório de todas as multas). O programa deverá
#imprimir tambémo número da carteira domotorista que obteve o maior número
#de multas.
#Obs.: O programa encerra ao ler a carteira de motorista de valor 0.

#23. Crie um programa que leia um conjunto de informações (nome, sexo, idade, peso
#e altura) dos atletas que participaram de uma olimpíada, e informar:
#• a atleta do sexo feminino mais alta;
#• o atleta do sexomasculinomais pesado;
#• amédia de idade dos atletas.
#Obs.: Deverão se lidos dados dos atletas até que seja digitado o nome @ para um
#atleta.
#Para resolver este exercício, consulte a aula 7 que aborda o tratamento de strings,
#como comparação e atribuição de textos.

#24. Faça um programa que calcule quantos litros de gasolina são usados em uma
#viagem, sabendo que um carro faz 10 km/litro. O usuário fornecerá a velocidade
#do carro e o período de tempo que viaja nesta velocidade para cada trecho do
#percurso. Então, usando as fórmulas distância = tempo x velocidade e litros
#consumidos = distância / 10, o programa computará, para todos os valores nãonegativos
#de velocidade, os litros de combustível consumidos. O programa deverá
#imprimir a distância e o número de litros de combustível gastos naquele trecho.
#Deverá imprimir também o total de litros gastos na viagem. O programa encerra
#quando o usuário informar umvalor negativo de velocidade.
#74 Aula 3. Estruturas de Iteração

#25. Faça umprograma que calcule o imposto de renda de umgrupo de contribuintes,
#considerando que:
#a) os dados de cada contribuinte (CIC, número de dependentes e renda bruta
#anual) serão fornecidos pelo usuário via teclado;
#b) para cada contribuinte será feito umabatimento de R$600 por dependente;
#c) a renda líquida é obtida diminuindo-se o abatimento com os dependentes
#da renda bruta anual;
#d) para saber quanto o contribuinte deve pagar de imposto, utiliza-se a tabela
#a seguir:
#Renda Líquida Imposto
#até R$1000 Isento
#de R$1001 a R$5000 15%
#acima de R$5000 25%
#e) o valor de CIC igual a zero indica final de dados;
#f ) o programa deverá imprimir, para cada contribuinte, o número do CIC e o
#imposto a ser pago;
#g) ao final o programa deverá imprimir o total do imposto arrecadado pela
#Receita Federal e o número de contribuintes isentos;
#h) leve em consideração o fato de o primeiro CIC informado poder ser zero.

#26. Foi feita uma pesquisa de audiência de canal de TV em várias casas de uma
#certa cidade, em umdeterminado dia. Para cada casa visitada foram fornecidos o
#número do canal (4, 5, 7, 12) e o número de pessoas que estavam assistindo a ele
#naquela casa. Se a televisão estivesse desligada, nada seria anotado, ou seja, esta
#casa não entraria na pesquisa. Criar um programa que:
#• Leia um número indeterminado de dados, isto é, o número do canal e o
#número de pessoas que estavam assistindo;
#• Calcule e imprima a porcentagem de audiência em cada canal.
#Obs.: Para encerrar a entrada de dados, digite o número do canal zero.

#27. Crie um programa que calcule e imprima o CR do período para os alunos de
#computação. Para cada aluno, o algoritmo deverá ler:
#• número da matrícula;
#• quantidade de disciplinas cursadas;
#• notas em cada disciplina;
#Além do CR de cada aluno, o programa deve imprimir o melhor CR dos
#alunos que cursaram5 ou mais disciplinas.
#• fim da entrada de dados é marcada por uma matrícula inválida (matrículas
#válidas de 1 a 5000);
#• CR do aluno é igual à média aritmética de suas notas.

#28. Construa umprograma que receba a idade, a altura e o peso de várias pessoas,
#Calcule e imprima:
#3.12. Exercícios da Aula 75
#• a quantidade de pessoas com idade superior a 50 anos;
#• amédia das alturas das pessoas com idade entre 10 e 20 anos;
#• a porcentagem de pessoas com peso inferior a 40 quilos entre todas as
#pessoas analisadas.

#29. Construa um programa que receba o valor e o código de várias mercadorias
#vendidas em umdeterminado dia. Os códigos obedecem a lista a seguir:
#L-limpeza
#A-Alimentação
#H-Higiene
#Calcule e imprima:
#• o total vendido naquele dia, com todos os códigos juntos;
#• o total vendido naquele dia em cada um dos códigos.
#Obs.: Para encerrar a entrada de dados, digite o valor da mercadoria zero.

#30. Faça um programa que receba a idade e o estado civil (C-casado, S-solteiro, Vviúvo
#e D-desquitado ou separado) de várias pessoas. Calcule e imprima:
#• a quantidade de pessoas casadas;
#• a quantidade de pessoas solteiras;
#• amédia das idades das pessoas viúvas;
#• a porcentagem de pessoas desquitadas ou separadas dentre todas as pessoas
#analisadas.
#Obs.: Para encerrar a entrada de dados, digite um número menor que zero para a
#idade.

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
    case 19: q19()
    case 20: q20()
    case 21: q21()
    case 22: q22()
    case 23: q23()
        