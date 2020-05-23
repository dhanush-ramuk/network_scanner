# network_scanner
A Simple Network Scanner that checks for open ports. It also convers domain name to ip address and vice versa.

## Examples 

1. python3 network_scanner.py google.com - **##converts the domain name to ip address**

2. python3 network_scanner.py 192.168.1.8 -
    **##converts the ip address to domain name**

3. python3 network_scanner.py -p 22 127.0.0.1 -
    **##checks if the specified port is open or not in the specified ip address or domain name**

4. python3 network_scanner.py -p 22-80 192.168.0.1 -
    **##checks if the specified range of ports are open or not in the specified ip address or domain name**
