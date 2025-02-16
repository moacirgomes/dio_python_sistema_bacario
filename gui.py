import time

def mostrar_extrato(saldo, extrato):
    print("================ EXTRATO ================")
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================================")
    time.sleep(2)  # Pausa de 2 segundos antes de limpar a tela

def exibir_menu():
    print("Opções:")
    print("d - Depositar")
    print("s - Sacar")
    print("e - Extrato")
    print("q - Sair")

def obter_opcao():
    return input("Escolha uma opção: ")
