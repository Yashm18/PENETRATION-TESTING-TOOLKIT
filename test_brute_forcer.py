from toolkit.brute_forcer import brute_force_login

def test_brute_force_login():
    result = brute_force_login("http://example.com/login", "admin", ["password"])
    assert result is None
