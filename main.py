import socket
import argparse
import sys
import logging
from __version__ import __version__
from banner import BANNER

logging.basicConfig(
    level=logging.INFO,
    filename='netsearch.log',
    format='%(asctime)s - [%(levelname)s] - %(message)s'
)

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='Domain to IP Resolver utility')

parser.add_argument('--version', action='version', version=f'NetSearch Version {__version__}', help='Show version')
parser.add_argument('domain', nargs='?', help='Domain to resolve')
args = parser.parse_args()

try:
    if not args.domain:
        print(BANNER)
        print('=' * 45)
        
    domain = args.domain or input('\n\u276f Enter a domain: ').strip()
    logger.info(f'Resolving domain: {domain}')

    try:
        ip = socket.gethostbyname(domain)
        logger.info(f'SUCCESS: {domain} \u2192 {ip}')
        print(f'[OK] IP for domain {domain} \u2192 {ip}')
    except socket.gaierror:
        logger.error(f'Domain not found: {domain}')
        print(f'[ERROR] Domain not found: {domain}')

except KeyboardInterrupt:
    print('\nCanceled by user.')
    logger.warning('Canceled by user [Ctrl+C]')
    sys.exit(0)