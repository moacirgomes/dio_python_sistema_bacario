import unittest
import dados_bancarios  # Importa o módulo inteiro
from operacoes import depositar, sacar, obter_extrato

class TestOperacoesBancarias(unittest.TestCase):

    def setUp(self):
        """Reseta os dados bancários antes de cada teste"""
        dados_bancarios.saldo = 100.0  # Saldo inicial
        dados_bancarios.extrato = ""  # Limpa o extrato
        dados_bancarios.numero_saques = 0  # Reseta contagem de saques

    def test_depositar(self):
        """Testa se o depósito está sendo realizado corretamente"""
        depositar(50.0)
        self.assertEqual(dados_bancarios.saldo, 150.0)
        self.assertIn("Depósito: R$ 50.00", dados_bancarios.extrato)

    def test_sacar_saldo_suficiente(self):
        """Testa saque quando há saldo suficiente"""
        mensagem = sacar(30.0)
        self.assertEqual(dados_bancarios.saldo, 70.0)
        self.assertIn("Saque: R$ 30.00", dados_bancarios.extrato)
        self.assertEqual(mensagem, "Saque de R$ 30.00 realizado com sucesso!")

    def test_sacar_saldo_insuficiente(self):
        """Testa tentativa de saque maior que o saldo disponível"""
        mensagem = sacar(150.0)
        self.assertEqual(dados_bancarios.saldo, 100.0)  # Saldo não deve mudar
        self.assertNotIn("Saque: R$ 150.00", dados_bancarios.extrato)
        self.assertEqual(mensagem, "Infelizmente você não possui saldo para essa transação!")
    
    def test_sacar_acima_do_limite_por_operacao(self):
        """Testa tentativa de saque acima do limite por operação"""
        mensagem = sacar(600.0)  # Supondo que o limite seja 500
        self.assertEqual(dados_bancarios.saldo, 100.0)  # Saldo não deve mudar
        self.assertEqual(mensagem, "Valor de saque excede o limite permitido de R$ 500.00.")
    
    def test_limite_maximo_saques(self):
        """Testa se o limite de saques diários é respeitado"""
        depositar(50.0)
        sacar(50.0)
        sacar(50.0)
        sacar(50.0)
        mensagem = sacar(50.0)  # Este saque não deve ser permitido
        self.assertEqual(dados_bancarios.numero_saques, 3)
        self.assertEqual(mensagem, "Número máximo de saques atingido!")
    
    def test_obter_extrato_apos_transacoes(self):
        """Testa se o extrato é gerado corretamente após depósitos e saques"""
        depositar(200.0)
        sacar(50.0)
        self.assertIn("Depósito: R$ 200.00", dados_bancarios.extrato)
        self.assertIn("Saque: R$ 50.00", dados_bancarios.extrato)
        self.assertEqual(dados_bancarios.saldo, 250.0)  # 100 + 200 - 50

if __name__ == '__main__':
    unittest.main()
