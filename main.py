import socket
import argparse
import sys
from __version__ import __version__
from banner import BANNER

parser = argparse.ArgumentParser(description='Domain to IP Resolver utility')

parser.add_argument('--version', action='version', version=f'NetSearch Version {__version__}', help='Show version')
parser.add_argument('domain', nargs='?', help='Domain to resolve')
args = parser.parse_args()

try:
    if not args.domain:
        print(BANNER)
        print('=' * 45)
        
        domain = args.domain or input('\n\u276f Enter a domain: ').strip()

    try:
        ip = socket.gethostbyname(domain)
        print(f'[OK] IP for domain {domain} \u2192 {ip}')
    except socket.gaierror:
        print(f'[ERROR] Domain not found: {domain}')

except KeyboardInterrupt:
    print('\nCanceled by user.')
    sys.exit(0)

