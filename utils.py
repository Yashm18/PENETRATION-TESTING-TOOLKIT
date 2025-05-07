import ipaddress

def is_valid_ip(ip: str) -> bool:
    """
    Validate an IP address.
    
    :param ip: IP address to validate.
    :return: True if valid, False otherwise.
    """
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False
