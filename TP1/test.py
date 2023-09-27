import fonctions as f
import pytest
import sys

def test_1 ():
    assert f.puissance(2 ,3) == 8
    assert f.puissance(2 ,2) == 4

def test_2():
    assert f.puissance(2, 5) == 2**5

def test_puissance_exception():
    with pytest.raises(ValueError):
        f.puissance(2, "trois")

def test_puissance_exception_2():
    with pytest.raises(ZeroDivisionError):
        f.puissance(2, 0)

def test_py_version():
    python_version = sys.version.split()[0]  # Get the first part of sys.version
    print("Python Version:", python_version)