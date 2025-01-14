import socket

ur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ROBOT_IP = '10.30.21.100'
ROBOT_PORT = 30002

ur.connect((ROBOT_IP, ROBOT_PORT))

def send_cmd(cmd):
    print(f'Executing `{cmd}`')
    ur.send(f'{cmd}\n'.encode())
    ur.recv(1024)

if __name__ == '__main__':
    s = input()
    while s.lower() != 'q' and s.lower() != 'quit':
        send_cmd(s)
        s = input()

#-247, -111, 147, 206, -90, 78
