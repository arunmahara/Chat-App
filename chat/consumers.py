
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

        self.room_name = self.scope['url_route']['kwargs']['roomName']
        #add channel to a new or existing group
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name
            )

        self.accept() #to accept connection continuously
        # self.close() #to reject connection immediately after connection 

    
    # this handler is called when data is received form client
    def receive(self, text_data=None, bytes_data=None):
        print('Message Received from client...', text_data)

        data = json.loads(text_data)   #converting string (json) data to python data to save message in database
        print(data)
        message = data['msg']
        room = Room.objects.get(name=self.room_name)
        if self.scope['user'].is_authenticated:  #user authentication

            data['user'] = self.scope['user'].username  #get user 
            user = data['user']
            username = User.objects.get(username = user)

            chat = Chat(room = room, user=username, message = message )
            chat.save()  # save data in data base for sync consumer

            async_to_sync(self.channel_layer.group_send)(self.room_name,{      # to send message to client form server 
                'type': 'chat.message',
                'message': message,
                'user':  user
            })



    # this handler is called when either connection to a client is lost , either form the client closing the connection, the server closing the connection or lost of the socket
    def disconnect(self, close_code):
        print('Websocket Disconnected...', close_code) 

         # disconnect channel group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name, self.channel_name
        )

        raise StopConsumer() 