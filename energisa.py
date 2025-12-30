def ler_valores():
    """Lê os valores do usuário e retorna um dicionário com as entradas.

    Mantém os prompts originais do script para compatibilidade.
    """
    def read_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print('Entrada inválida. Digite um número.')

    valores = {}
    valores['mediaTenA'] = read_float('Digite o Valor da Tensão Média A: ')
    valores['mediaTenB'] = read_float('Digite o Valor da Tensão Média B: ')
    valores['mediaTenc'] = read_float('Digite o Valor da Tensão Média c: ')

    valores['correntePrimariaA'] = read_float('Digite o Valor da Corrente Primária A: ')
    valores['correntePrimariaB'] = read_float('Digite o Valor da Corrente Primária B: ')
    valores['correntePrimariaC'] = read_float('Digite o Valor da Corrente Primária C: ')

    valores['correnteSecundariaA'] = read_float('Digite o Valor da Corrente Secundária A: ')
    valores['correnteSecundariaB'] = read_float('Digite o Valor da Corrente Secundária B: ')
    valores['correnteSecundariaC'] = read_float('Digite o Valor da Corrente Secundária C: ')

    valores['Tranformadordecorrente'] = read_float('Qual Valor do TC: ')
    valores['fatordepotencia'] = read_float('Qual Fator de Pontência: ')
    valores['demanda'] = read_float('CAMPO 16: ')
    return valores


def relacao_tc(tc_valor: float) -> float:
    return tc_valor / 5


def calcular_dm(media_tensoes: float, divisao_sec: float, relacao_tc_val: float, fp: float, raiz: float = 1.73) -> float:
    return (media_tensoes * divisao_sec * relacao_tc_val * fp * raiz) / 1000


def percent_error(dm: float, demanda: float, resultadoTrasnformador: float) -> float:
    y = resultadoTrasnformador * demanda
    if dm == 0 and y == 0:
        return 0.0
    if dm == 0 or y == 0:
        return float('inf')
    if dm > y:
        x = dm / y
        r = x * 100
        s = r - 100
        return s
    elif y > dm:
        x = y / dm
        r = x * 100
        s = r - 100
        return s
    return 0.0


def main():
    raiz = 1.73
    v = ler_valores()

    resultadoFF = ((v['mediaTenA'] + v['mediaTenB'] + v['mediaTenc']) / 3)
    print(f'A MEDIA DAS TENSÃO: {resultadoFF:.2f}')

    resultadoTrasnformador = relacao_tc(v['Tranformadordecorrente'])
    print(f'Relação do TC: {resultadoTrasnformador:.2f}')

    divisaoDASPrimaria = ((v['correnteSecundariaA'] + v['correnteSecundariaB'] + v['correnteSecundariaC']) / 3)

    resultadoSecundariaA = (resultadoTrasnformador * v['correnteSecundariaA'])
    resultadoSecundariaB = (resultadoTrasnformador * v['correnteSecundariaB'])
    resultadoSecundariaC = (resultadoTrasnformador * v['correnteSecundariaC'])

    print(f'Resultado Corrente Primaria A : [{resultadoSecundariaA:.2f}]')
    print(f'Resultado Corrente Primaria B :[{resultadoSecundariaB:.2f}]')
    print(f'Resultado Corrente Primaria C: [{resultadoSecundariaC:.2f}]')

    print(f'Resultados das Correntes Dividido Por TC: [{divisaoDASPrimaria}]')

    print(f'Valor IpA :{v["correntePrimariaA"]}, E Corrente Secundária A: {resultadoSecundariaA:.2f}')
    print(f'Valor IpB: {v["correntePrimariaB"]}, E Corrente Secundária B: {resultadoSecundariaB:.2f}')
    print(f'Valor IpC: {v["correntePrimariaC"]}, E Corrente Secundária c: {resultadoSecundariaC:.2f}')

    dm = calcular_dm(resultadoFF, divisaoDASPrimaria, resultadoTrasnformador, v['fatordepotencia'], raiz)
    print(f'DM >>>:{dm:.2f}')

    s = percent_error(dm, v['demanda'], resultadoTrasnformador)
    if s == float('inf'):
        print('Porcentagem de ERROR Final: infinito (divisão por zero)')
    else:
        print(f'Porcentagem de ERROR Final: {s:.2f}')


if __name__ == '__main__':
    main()
