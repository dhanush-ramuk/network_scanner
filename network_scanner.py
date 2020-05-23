#!/bin/python3

"""
Simple Network Scanner. It checks for the open ports in the specified ip address, converts ip address to domain name and vice versa.
"""

import socket
import sys
import argparse


class Network_Utility:
	def find_ports(self, ports):
		if ports.find('-') == -1:
			return -1, int(ports)
		else:
			return int(ports[0 : ports.index('-')]), int(ports[(ports.index('-')+1) : ])
		
	def find_ip_or_domain(self, value):
		if value[-1].isdigit():
			self.ip_to_domain(value)
		else:
			self.domain_to_ip(value)
			
			
	def domain_to_ip(self, domain_name):
		try:
			print("domain name:{}\nip address:{} ".format(domain_name, socket.gethostbyname(domain_name)))
			
		except socket.gaierror:
			print("Given wrong domain or ip address")
			sys.exit()
			
	
	def ip_to_domain(self, ip_addr):
		try:
			(hostname, aliaslist, ipaddrlist) = socket.gethostbyaddr(ip_addr)
			print("ip address:{}\ndomain name:{}".format(ip_addr, hostname))
		except socket.gaierror:
			print("Given wrong domain or ip address")
			sys.exit()
			
	def scan_ports(self, ports, domain_name):
		try:
			startPort, endPort = self.find_ports(ports)
			if startPort == -1:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.setdefaulttimeout(1)
				result = s.connect_ex((domain_name, endPort))
				if result == 0:
					print("Port {} is open".format(endPort))
					s.close
				else:
					print("Port {} is closed".format(endPort))
			else:
				
				for port in range(startPort, endPort+1):
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					socket.setdefaulttimeout(1)
					result = s.connect_ex((domain_name, port))
					if result == 0:
						print("Port {} is open".format(port))
					else:
						print("Port {} is closed".format(port))
		except KeyboardInterrupt:
			print("\nExiting Program")
			sys.exit()
		except socket.gaierror:
			print("\nGiven wrong domain or ip address")
		



parser = argparse.ArgumentParser(description="Open Source Network Scanner. Scans for ports, converts domain name to ip address, and vice-versa.")
parser.add_argument("ip_value", help="ip address value or domain name for scanning ports and conversion. Examples for ip to domain and vice-versa \"python3 network_scanner 192.168.1.1\", \"python3 network_scanner google.com\"", type=str)
parser.add_argument("-p", "--port", default=0, help="Enables port scanner. Specify port or range of port value along with it. \
Examples \"python3 network_scanner -p 80 google.com\", \
	\"python3 network_scanner -p 20-80 127.0.0.1\"")
args = parser.parse_args()
obj = Network_Utility();
if args.port:
	obj.scan_ports(args.port, sys.argv[3])
	
else:
	obj.find_ip_or_domain(sys.argv[1])





