import socket

MCAST_GRP = '239.255.255.250'
MCAST_PORT = 1900
MSEARCH_MSG = ('M-SEARCH * HTTP/1.1\r\n' +
                'HOST: ' + MCAST_GRP + ':' + str(MCAST_PORT) + '\r\n')

timeout = 5
encontrado = False

socket.setdefaulttimeout(timeout)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.bind(('', MCAST_PORT))
s.sendto(MSEARCH_MSG.encode(), (MCAST_GRP, MCAST_PORT))

while True:
    try:
        data, addr = s.recvfrom(65507)
        if data:
            print('Encontrado:', data.decode())
            encontrado = True
            break
    except:
        print('Timeout')
        break

print("Proceso terminado")
s.close()


