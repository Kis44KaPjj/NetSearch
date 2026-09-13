import socket
import argparse
from __version__ import __version__
from banner import BANNER

parser = argparse.ArgumentParser(description='Domain to IP Resolver utility')

parser.add_argument('--version', action='version', version=f'NetSearch Version {__version__}', help='Show version')
args = parser.parse_args()

print(BANNER)
print('=' * 48)

while True:
    domain = input('\n\u276f Enter a domain: ').strip()

    if domain.lower() == 'q':
        print('Exiting...')
        break

    try:
        ip = socket.gethostbyname(domain)
        print(f'[OK] IP for domain {domain} \u2192 {ip}')
    except socket.gaierror:
        print(f'[ERROR] Domain not found: {domain}')