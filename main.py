import argparse
from toolkit.port_scanner import scan_ports
from toolkit.brute_forcer import brute_force_login
from toolkit.vulnerability_scanner import test_sql_injection, test_xss
from toolkit.utils import is_valid_ip

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    # Port Scanner
    port_parser = subparsers.add_parser("scan", help="Scan open ports on a target")
    port_parser.add_argument("target", help="Target IP address")
    port_parser.add_argument("--start", type=int, default=1, help="Starting port")
    port_parser.add_argument("--end", type=int, default=1024, help="Ending port")

    # Brute Forcer
    brute_parser = subparsers.add_parser("brute", help="Perform a brute-force attack")
    brute_parser.add_argument("url", help="Login page URL")
    brute_parser.add_argument("username", help="Username to test")
    brute_parser.add_argument("password_file", help="File containing password list")

    # Vulnerability Scanner
    vuln_parser = subparsers.add_parser("vuln", help="Test for vulnerabilities")
    vuln_parser.add_argument("url", help="URL to test")
    vuln_parser.add_argument("param", help="Parameter to test")

    args = parser.parse_args()

    if args.command == "scan":
        if not is_valid_ip(args.target):
            print("Invalid IP address")
            return
        open_ports = scan_ports(args.target, args.start, args.end)
        print(f"Open ports: {open_ports}")

    elif args.command == "brute":
        with open(args.password_file, "r") as f:
            passwords = f.read().splitlines()
        result = brute_force_login(args.url, args.username, passwords)
        if result:
            print(f"Login successful: {result}")
        else:
            print("Login failed")

    elif args.command == "vuln":
        if test_sql_injection(args.url, args.param):
            print("SQL Injection vulnerability found!")
        if test_xss(args.url, args.param):
            print("XSS vulnerability found!")

if __name__ == "__main__":
    main()
