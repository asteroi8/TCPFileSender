import socket
import _thread
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
    totalsent = 0
    data = readFile()
    while totalsent < len(data):
        sent = clientsock.send(bytes(data, 'UTF-8'))
        if sent == 0:
            raise RUNtimeError("socket connection broken")
        totalsent = totalsent + sent
    clientsock.shutdown(1)

if __name__=='__main__':
    #create tcp socket
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #setup socket
    server_address = ("", 4002)
    socket.bind(server_address)

    #listen for connections n=5
    socket.listen(5)

    while True:
        #when client connections made, read from file and send to client socket
        connection, client = socket.accept()

        try:
            print(sys.stderr, "waiting for connection")
        #unfortunately keeps reading and sending the
                #data but only to one client connection
            #read and send data to
            while connection:                
                if readFile():
                    #send data over socket
                    sendData(connection, client)
                    #threaded
                   #_thread.start_new_thread(sendData, (connection, client))
                else:
                    print(sys.stderr, "sorry bru no more data")
                    break
        finally:
            #clean up the connection
            connection.close()
            
                                        
#create thread for sending data on each connection
