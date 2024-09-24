import os

def a_capo():
    print('\n')

def Line():
    print('- - - - - - -')

os.system('figlet -f slant RouterMinicom && sleep 1')
a_capo()

os.system('lsusb')
a_capo()

os.system('dmesg | grep tty')
a_capo()

print('\n! Remember the baud configuration ! (Es: -> 9600 baud)\n')

Porta = input('Choose port name (tree, Es: /dev/ttyUSB0): ')
Line()

os.system(f"sudo minicom -D {Porta} -b 9600")
