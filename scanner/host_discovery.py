"""
host_discovery_nmaplib.py
--------------------------

Performs host discovery using python-nmap.

Functions:
- get_local_subnet(): Detects the CIDR block of your current local IP
- discover_hosts(): Should discover all Ips and store them in a list to later be port scanned
"""

import socket
import nmap
