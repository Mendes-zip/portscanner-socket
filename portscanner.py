import socket



def scan(target, ports):
	print('\n' + ' Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target,port)


def scan_port(ip, port):
	try:
		sock = socket.socket()
		sock.connect((ip, port))
		print("[+] Port Open " + str(port))
		sock.close()
	except:
		pass


targets = input("[*] Alvo para escanear (separados por vírgula ,): ")
ports = int(input("[*]Quantas portas você quer escanear?: "))
if ',' in targets:
	print("[*] Scanning Multiple Targets")
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
