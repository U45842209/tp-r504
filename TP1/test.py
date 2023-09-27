import fonctions as f
import pytest

def test_1 ():
    assert f.puissance(2 ,3) == 8
    assert f.puissance(2 ,2) == 4

def test_2():
    assert f.puissance(2, 5) == 2**5