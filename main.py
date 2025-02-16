import time
from gui import exibir_menu, obter_opcao
from operacoes import depositar, sacar, obter_extrato
from utils import limpar_tela, obter_valor

# Exemplo de uso
while True:
    limpar_tela()  # Limpa a tela a cada iteração do loop
    exibir_menu()
    opcao = obter_opcao()

    if opcao == "d":
        valor_deposito = obter_valor()
        depositar(valor_deposito)
    elif opcao == "s":
        valor_saque = obter_valor()
        mensagem = sacar(valor_saque)
        print(mensagem)
    elif opcao == "e":
        obter_extrato()
    elif opcao == "q":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
    time.sleep(2)  # Pausa de 2 segundos antes de limpar a tela
