import fonctions as f
import pytest

def test_1 ():
    assert f.puissance(2 ,3) == 8
    assert f.puissance(2 ,2) == 4

def test_2():
    assert f.puissance(2, 5) == 2**5

def test_puissance_exception():
    with pytest.raises(ValueError):
        f.puissance(2, "trois")
        f.puissance(a=2,b=-3)

def test_puissance_exception_2():
    with pytest.raises(ZeroDivisionError):
        f.puissance(2, 0)