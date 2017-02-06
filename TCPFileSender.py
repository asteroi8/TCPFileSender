import socket
import sys


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
    
if __name__=='__main__':
    #create tcp socket
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     #forcibly bind to port in use
    _socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #setup socket
    server_address = ("", 4002)
    socket.bind(server_address)

    #listen for connections n=5
    socket.listen(5)

   while True:
        #when client connections made, read from file and send to client socket
        connection, client = _socket.accept()
        
        try:
            print(sys.stderr, "waiting for connection")
            #unfortunately keeps reading and sending the
                #data but only to one client connection
            #read and send data to               
            if readFile():
                #send data over socket
                sendData(connection, client)
            else:
                print(sys.stderr, "sorry bru no more data")
                break
        finally:
            #clean up the connection
            connection.close()
