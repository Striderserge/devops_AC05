import pytest
from com.ope.calcula_parcela import valorPagamento

def test_calcula_parcela1():
    assert valorPagamento(10,5) == 10.8, "Deverá ser 10.8"

def test_calcula_parcela2():
    assert valorPagamento(-5,0) == None, "Deverá ser None"
    
def test_calcula_parcela3():
    assert valorPagamento(10,0) == 10, "Deverá ser 10"

