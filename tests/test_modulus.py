from src.modulus import modulus

def test_modulus():
    assert modulus(10,3) == 1
    assert modulus(9,3) == 0
    assert modulus(15,4) == 3


