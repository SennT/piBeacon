#  **************************************************************
#   Projekt         : Pibeacon
#   Modul           : rfcomm.server
#  --------------------------------------------------------------
#   Autor(en)       : Timo Senn
#   Beginn-Datum    : 30.04.2017
#  --------------------------------------------------------------
#   Beschreibung    : RFCOMM-Server for pairing
#  --------------------------------------------------------------
#
#  **************************************************************
#   Änderungs-Protokoll:
#  --------------------------------------------------------------
#   wann                 wer   was
#   10.05.2017           TS    Adding Checkbox for Pairing
#  --------------------------------------------------------------
import bluetooth
import socket
import _thread
from comm.intcomm import IntComm
from comm.intmessage import IntMessage as IntMsg

class Server(IntComm):

   _commCallback = None

   def __init__(self, commCallback):
        self._commCallback = commCallback

   def comm(self, msg):
        pass
   
   def startServer(self):
         
        print ("Starting server")
        server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

        port = 1
        server_sock.bind(("",port))
        server_sock.listen(1)
        port = server_sock.getsockname()[1]

        self._commCallback(IntMsg(IntMsg.SIGNAL_DHBWBEACON, {'DATA': 'Started new Server on Socket ' + str(port)}))


        self._commCallback(IntMsg(IntMsg.SIGNAL_DHBWBEACON, {'DATA': 'Waiting for connection on RFCOMM channel %d' % port}))

        client_sock,address = server_sock.accept()

        self._commCallback(IntMsg(IntMsg.SIGNAL_DHBWBEACON, {'DATA': 'Accepted connection from ' + address}))

        self._commCallback(IntMsg(IntMsg.SIGNAL_DHBWBEACON, {'disconnected' + str(client_info)}))
        client_sock.close()
        server_sock.close()

