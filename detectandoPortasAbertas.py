# -*- coding: utf-8
import socket
from sys import argv

class ScanPort:
    def __init__(self, ip):
        self.ip = 0
        self.set_Endereco(ip)
        for port in range(1, 65535):
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if client.connect_ex((self.ip, port)) == 0:
                print("[ Porta ] ===:> ",port, " = aberta")
            else:
               #print("Porta {} [FECHADA]".format(port))
                client.close()

    def set_Endereco(self, end):
        self.ip = end

    def get_Retorno(self):
        return self.ip

ip ="localhost"# argv[1]
buscar = ScanPort(ip=ip)
print(buscar.get_Retorno())