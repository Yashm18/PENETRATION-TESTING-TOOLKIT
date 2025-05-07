from toolkit.utils import is_valid_ip

def test_is_valid_ip():
    assert is_valid_ip("192.168.1.1") == True
    assert is_valid_ip("invalid_ip") == False
