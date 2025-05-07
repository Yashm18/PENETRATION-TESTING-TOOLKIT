from toolkit.port_scanner import scan_ports

def test_scan_ports():
    open_ports = scan_ports("127.0.0.1", 79, 81)
    assert isinstance(open_ports, list)
