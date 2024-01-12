#import necessary dependencies
import requests
import socket
import requests
import OS

# Create a function scan_ports
# Target IP and List of ports to scan

def scan_ports(target_ip, ports):
  open_ports = []
  for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        open.ports.append(port)
      sock.close()
return open_ports

#Example Target Port
target_ip = '192.168.1.1'
ports_to_scan = range(1, 1025)
open_ports = scan.ports(target_ip,ports_to_scan)
print(f"Open ports: {open_ports}")

#Web Testing

def check_vulnerable_url(url):
  response = requests.get(url)
  if response.status_code == 200:
    # checking for specific vulnerabilities
    # ie; Sql injection, XSS
    if 'vulnerable' in response.text:
      return 'Vulnerable'
    return 'Not vulnerable'

# Quick Example
# input your own
# Send HTTP GET request to the target URL and check specific vulnerability 

target_url = 'http://example.com'
result = check_vulnerable_url(target_url)
print(f"target URL is {result}")

# Replace this with an actual exploit of your choice

def exploit_vulnerability():
  # Example: os.system("exploit_command_here")
  print("Exploit code executed successfully.")

exploit_vulnerability()


