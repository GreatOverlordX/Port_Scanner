import socket,sys
import pyfiglet

ascii_banner = pyfiglet.figlet_format("WELCOME \nUwU \n Pentesting   with python \nWritten   by : GreatOverlordX")  # CLI introductory text
print(ascii_banner)

ip = f'{sys.argv[1]}'
open_ports = []

ports = range(1, 65535)  # You may edit this.

def probe_port(ip, port, result =1 ):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        r = sock.connect_ex((ip, port))
        if r == 0:
            result = r
        sock.close()
    except Exception as e:
        pass
    return result

for port in ports:
    sys.stdout.flush()
    response = probe_port(ip, port)
    if response == 0:
        open_ports.append(port)
        
    if open_ports:
        print('Open Ports are: ')
        print(sorted(open_ports))
    else: 
        print('Oops :( ! Looks like no ports are open')
