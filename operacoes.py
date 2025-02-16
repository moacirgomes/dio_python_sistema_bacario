import time
import dados_bancarios  # Importa o módulo inteiro
from gui import mostrar_extrato

def depositar(valor):
    """Deposita um valor na conta e atualiza o extrato corretamente"""
    dados_bancarios.saldo += valor  # Modifica diretamente a variável no módulo
    dados_bancarios.extrato += f"Depósito: R$ {valor:.2f}\n"
    print(f"Novo saldo: R$ {dados_bancarios.saldo:.2f}")
    time.sleep(2)

def sacar(valor):
    """Realiza saque verificando saldo e limites"""
    if dados_bancarios.numero_saques < dados_bancarios.LIMITE_SAQUES and valor <= dados_bancarios.limite_saque_operacao:
        if dados_bancarios.saldo < valor:
            return "Infelizmente você não possui saldo para essa transação!"
        else:
            dados_bancarios.saldo -= valor
            dados_bancarios.numero_saques += 1
            dados_bancarios.extrato += f"Saque: R$ {valor:.2f}\n"
            time.sleep(2)
            return f"Saque de R$ {valor:.2f} realizado com sucesso!"
    else:
        if dados_bancarios.numero_saques >= dados_bancarios.LIMITE_SAQUES:
            return "Número máximo de saques atingido!"
        else:
            return f"Valor de saque excede o limite permitido de R$ {dados_bancarios.limite_saque_operacao:.2f}."

def obter_extrato():
    """Exibe o extrato atual"""
    mostrar_extrato(dados_bancarios.saldo, dados_bancarios.extrato)
