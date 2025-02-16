import os

def limpar_tela():
    # Se for Windows, usa 'cls', senão (Linux e Mac) usa 'clear'
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def obter_valor():
    while True:
        valor_str = input("Informe o valor: ")
        try:
            valor = float(valor_str)
            if valor > 0:
                return valor
            else:
                print("Por favor, insira um valor positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
