"""
port_scanner.py
----------------

Scans a target host for open TCP ports using multi-threaded socket connections.
Includes integration with banner grabbing for basic service fingerprinting.

Functions:
- scan_port(ip, port, timeout): Attempts to connect and grab banner from a specific port.
- scan_ports(ip, ports): Scans a list of ports on a given IP and returns (port, banner) tuples.
"""
