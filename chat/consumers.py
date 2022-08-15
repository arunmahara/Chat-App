
from tokenize import group
from channels.exceptions import StopConsumer
import json
from asgiref.sync import async_to_sync
from .models import Chat, Room
from django.contrib.auth.models import User
from channels.generic.websocket import WebsocketConsumer
 
# GENERIC SYNC-WEBSOCKET-CONSUMER
class MyWebsocketConsumer(WebsocketConsumer):

    # this handler is called when client initially opens a connection and is about to finish the WebSocket Handshake
    def connect(self):
        print('Websocket Connected...')


        self.accept() #to accept connection continuously

    
    # this handler is called when data is received form client
    def receive(self, text_data=None, bytes_data=None):
        pass

    # this handler is called when either connection to a client is lost , either form the client closing the connection, the server closing the connection or lost of the socket
    def disconnect(self, close_code):
        print('Websocket Disconnected...', close_code) 

        raise StopConsumer() 