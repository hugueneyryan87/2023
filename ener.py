dm = 67.88
resultadoFF = 392
divisaoDASPrimaria = 1.33
resultadoTrasnformador = 80
raiz = 1.73
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