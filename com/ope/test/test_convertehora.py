import pytest
from com.ope import converte_hora


def test_hora1():
    assert converte_hora.converteHora(25,0) == None , "Deve retornar nulo"

def test_hora2():
    assert converte_hora.converteHora(10,10) == '10:10 AM', "deve ser 10:10AM"

def test_hora3():
    assert converte_hora.converteHora(23,10) == '11:10 PM', "deve ser 11:10PM"  

def test_hora4():
    assert converte_hora.converteHora(0,10) == '12:10 AM', "deve ser 12:10AM"


