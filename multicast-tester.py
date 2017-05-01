#
# Test multicast traffic
#
import argparse
import socket
import struct
import sys


def parseArguments():
    parser = argparse.ArgumentParser(description='Multicast client/server')

    parser.add_argument('-c', '--client', action='store_true', help='Start this instance as a client,  sending out a message on a given multicast address/port')
    parser.add_argument('-s', '--server', action='store_true', help='Start this instance as a server, listening on the multicast address')
    parser.add_argument('-p', '--port', type=int, action='store', help='Port to listen/connect on')
    parser.add_argument('-a', '--address', action='store', help='Multicast address to listen/connect')
    parser.add_argument('-m', '--message', action='store', help='Message to send from the server')
    parser.add_argument('-t', '--ttl', type=int, action='store', help='Time to Live for packets, how many segments to route through' )
    parser.add_argument('-w', '--wait', type=float, action='store', help='Time to wait to recieve messages' )

    return parser.parse_args()


def createClientSocket(address, port, ttl):
    addressAndPort = (address, port)
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ttl = struct.pack('b', ttl)
    clientSocket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
    clientSocket.connect(addressAndPort)
    return clientSocket


def createServerSocket(address, port, receiveTimeout):
    addressAsInt = socket.inet_aton(address)
    addressAsStruct = struct.pack('4sL', addressAsInt, socket.INADDR_ANY)

    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, addressAsStruct)
    serverSocket.settimeout(receiveTimeout)
    serverSocket.bind('', port)
    return serverSocket


def serverReceiveLoop(serverSocket):
    while True:
        try:
            data, clientAddress = serverSocket.recvfrom(100)
        except socket.timeout:
            print >>sys.stderr, 'Timed out waiting for data'
            continue
        except Exception as ex:
            print >>sys.stderr, 'Received exception %s' % ex
            break


def clientSendLoop(clientSocket):
    while True:


# ########### #
# MAIN SCRIPT #
# ########### #

arguments = parseArguments()

if arguments.client and arguments.server:
    print >>sys.stderr,  'Make your mind up, client OR server'
    exit(1)
