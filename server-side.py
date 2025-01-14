import socket
import math

ur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ROBOT_IP = '10.30.21.100'
ROBOT_PORT = 30002

ur.connect((ROBOT_IP, ROBOT_PORT))
print(f'Connected to UR robot at {ROBOT_IP}:{ROBOT_PORT}.')

def send_cmd(cmd):
    print(f'Executing `{cmd}`')
    ur.send(f'{cmd}\n'.encode())
    ur.recv(1024)

def movej_degrees(target, a=1.0, v=0.1):
    radians = [0 for i in target]
    for i, degs in enumerate(target):
        radians[i] = math.radians(degs)
    send_cmd(f'movej({radians}, a={a}, v={v})')

if __name__ == '__main__':
    s = input()
    while s.lower() != 'q' and s.lower() != 'quit':
        send_cmd(s)
        s = input()

#-247, -111, 147, 206, -90, 78
