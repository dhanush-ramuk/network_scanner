#!/bin/python3

"""
Simple Network Scanner. It checks for the open ports in the specified ip address, converts ip address to domain name and vice versa.
"""

import socket
import sys
import argparse




class Network_Utility:
	def parse_arguments(self):
		parser = argparse.ArgumentParser(description="Open Source Network Scanner. Scans for ports, converts domain name to ip address, and vice-versa.")
		parser.add_argument("ip_value", help="ip address value or domain name for scanning ports and conversion. Examples for ip to domain and vice-versa \"python3 network_scanner 192.168.1.1\", \"python3 network_scanner google.com\"", type=str)
		parser.add_argument("-p", "--port", default=0, help="Enables port scanner. Specify port or range of port value along with it. \
Examples \"python3 network_scanner -p 80 google.com\", \
	\"python3 network_scanner -p 20-80 127.0.0.1\"")
		args = parser.parse_args()
		return args
		
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
	
	def create_socket(self, domain_name, port):
		socket.setdefaulttimeout(1)
		return socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex((domain_name, port))
			
			
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
			
		
				
	def scan_ports_multiprocessing(self, port, domain_name):
		try:		
			result = self.create_socket(domain_name, port)
			if result == 0:
				print("Port {} is open".format(port))
			else:
				print("Port {} is closed".format(port))			
					
		except KeyboardInterrupt:
			print("\nExiting Program")
			sys.exit()
		except socket.gaierror:
			print("\nGiven wrong domain or ip address")
		




if __name__ == "__main__":
	obj = Network_Utility()
	args = obj.parse_arguments()
	if args.port:
		startPort, endPort = obj.find_ports(args.port)
		if startPort == -1:
			obj.scan_ports_multiprocessing(endPort, sys.argv[3])
		else:
			for port in range(startPort, endPort+1):
				obj.scan_ports_multiprocessing(port, sys.argv[3])

							
	else:
		obj.find_ip_or_domain(sys.argv[1])







"""
without multiprocessing, checking 0-100 ports on 192.168.1.8, time taken is 0.0180

"""

