import pytest

from com.ope import conta_corrente

def teste1():
    conta = conta_corrente.ContaCorrente(1234, "LucasPizza", 5)
    conta.alterarNome("LucasPiza")
    conta.deposito(1500)
    conta.saque(500)