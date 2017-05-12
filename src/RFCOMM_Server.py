import bluetooth

class Server():
    def startServer():
        print ("Starting server")
        server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

        port = 1
        server_sock.bind(("",port))
        server_sock.listen(1)

        print ("Server is up")
        client_sock,address = server_sock.accept()
        print ("Accepted connection from ",address)

        data = client_sock.recv(1024)
        print ("received [%s]" % data)

    def stopServer():
        client_sock.close()
        server_sock.close()
