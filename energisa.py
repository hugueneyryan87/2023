correntePrimariaA = 0
correntePrimariaB = 0
correntePrimariaC = 0
Tranformadordecorrente = 0
ipA = 0
ipB = 0
ipC = 0
divisaoDASPrimaria = 0
variavelfinal = 0
raiz = 1.73 
mediaTenA = float(input('Digite o Valor da Tensão Média A: '))
mediaTenB = float(input('Digite o Valor da Tensão Média B: '))
mediaTenc = float(input('Digite o Valor da Tensão Média c: '))
resultadoFF = ((mediaTenA + mediaTenB + mediaTenc)/3)

print(F'A MEDIA DAS TENSÃO: {resultadoFF:.2f}')

correntePrimariaA = float(input('Digite o Valor da Corrente Primária A: '))
correntePrimariaB = float(input('Digite o Valor da Corrente Primária B: '))
correntePrimariaC = float(input('Digite o Valor da Corrente Primária C: '))


correnteSecundariaA = float(input('Digite o Valor da Corrente Secundária A: '))
correnteSecundariaB = float(input('Digite o Valor da Corrente Secundária B: '))
correnteSecundariaC = float(input('Digite o Valor da Corrente Secundária C: '))


Tranformadordecorrente = float(input('Qual Valor do TC: '))
resultadoTrasnformador = (Tranformadordecorrente/5)
print(f'Relação do TC: {resultadoTrasnformador:.2f}')
divisaoDASPrimaria = ((correnteSecundariaA + correnteSecundariaB + correnteSecundariaC)/3)

resultadoSecundariaA = (resultadoTrasnformador * correnteSecundariaA)
print(f'Resultado Corrente Primaria A : [{resultadoSecundariaA:.2f}]')
    
resultadoSecundariaB = (resultadoTrasnformador * correnteSecundariaB)
print(f'Resultado Corrente Primaria B :[{resultadoSecundariaB:.2f}]')
    
resultadoSecundariaC = (resultadoTrasnformador * correnteSecundariaC)
print(f'Resultado Corrente Primaria C: [{resultadoSecundariaC:.2f}]')
    

    
print(f'Resultados das Correntes Dividido Por TC: [{divisaoDASPrimaria}]')

print(f'Valor IpA :{correntePrimariaA}, E Corrente Secundária A: {resultadoSecundariaA:.2f}')

print(f'Valor IpB: {correntePrimariaB}, E Corrente Secundária B: {resultadoSecundariaB:.2f}') 

print(f'Valor IpC: {correntePrimariaC}, E Corrente Secundária c: {resultadoSecundariaC:.2f}')

fatordepotencia = float(input('Qual Fator de Pontência: '))
dm = ((resultadoFF * divisaoDASPrimaria * resultadoTrasnformador * fatordepotencia * raiz)/1000)
print(f'DM >>>:{dm:.2f}')
demanda = float(input(f'CAMPO 16: '))
y = resultadoTrasnformador * demanda
if dm > y :
    x = dm / y
    r = x *100
    s = r - 100
    print(f'Porcentagem de ERROR Final: {s:2f}')  
if y > dm :
    x = y/ dm
    r = x *100
    s = r - 100
    print(f'Porcentagem de ERROR Final: {s:2f}')     
