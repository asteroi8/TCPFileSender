import socket
import sys

#file write
def createFile():
    with open('file_object.txt', 'w') as fileContent:
        fileContent.write("no mas\n")
        fileContent.close()

#file read
def readFile():
    #open file object
    with open('file_object.txt', 'r') as fileContent:
        content = fileContent.readline()
        if content is None:
            fileContent.close()          
    return content

#handler for sending data to clients
def sendData(clientsock,addr):
    data = readFile()
    clientsock.send(bytes(data, 'UTF-8'))

def setupServer(address, port):
    # create tcp socket
    _socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # forcibly bind to port in use
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # setup socket
    server_address = (address, port)

    _socket.bind(server_address)

    return _socket


def runServer(sock):
    # create that file here
    createFile()
    ## listen for connections n=5
    sock.listen(5)

    while True:
    # when client connections made, read from file and send to client socket
        connection, client = sock.accept()
        client_address = client

        try:
            print(sys.stderr, "waiting for connection")
            # unfortunately keeps reading and sending the
            # data but only to one client connection
            # read and send data to
            if readFile():
                # send data over socket
                sendData(connection, client)
            else:
                print(sys.stderr, "sorry bru no more data")
        finally:
            # clean up the connection
            print(client)
            connection.close()

if __name__=='__main__':

    server_socket = setupServer("", 4006)

    runServer(server_socket)


