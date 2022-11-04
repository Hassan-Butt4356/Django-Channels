from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio
import json
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async

from channels.generic.websocket import(
     WebsocketConsumer,
     AsyncWebsocketConsumer,
     JsonWebsocketConsumer,
     AsyncJsonWebsocketConsumer

)
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('Connected',event)
        print('Channel Layer...',self.channel_layer)
        print('Channel Layer...',self.channel_name)

        #adding channel to an existing group
        async_to_sync(self.channel_layer.group_add)('group_name',self.channel_name)

        self.send({
            'type':'websocket.accept'
        })

    def websocket_receive(self,event):
        # print('Received',event)
        # data=json.loads(event['text'])
        # print(data)
        # print('Text',data['msg'])
        print('Data From Client',event['text'])

        async_to_sync(self.channel_layer.group_send)(
            'group_name',{
                'type':'chat.message',
                'message':event['text']
            }
        )
        # for i in range(5):
        #     self.send({
        #         'type':'websocket.send',
        #         'text':f'Message from Server {i}'
        #     })
        #     sleep(1)

    def chat_message(self,event):
        print('Actual Data',event['message'])
        self.send({
            'type':'websocket.send',
            'text':event['message']
        })

    def websocket_disconnect(self,event):
        print('Disconnected',event)
        print('Channel Layer...',self.channel_layer)
        print('Channel Layer...',self.channel_name)

        #removing channel from group when connection is lost
        async_to_sync(self.channel_layer.group_discard)('group_name',self.channel_name)
        raise StopConsumer()

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        
        print('Connected',event)
        print('Channel Layer...',self.channel_layer)
        print('Channel Layer...',self.channel_name)

        #adding channel to an existing group
        await self.channel_layer.group_add('group_name',self.channel_name)

        await self.send({
            'type':'websocket.accept'
        })

    async def websocket_receive(self,event):
        print('Received',event)
        print('Text',event['text'])
        print('Data From Client',event['text'])

        await self.channel_layer.group_send(
            'group_name',{
                'type':'chat.message',
                'message':event['text']
            }
        )
        # for i in range(5):
        #     await self.send({
        #         'type':'websocket.send',
        #         'text':f'Message from Server {i}'
        #     })
        #     await asyncio.sleep(1)

    async def chat_message(self,event):
        print('Actual Data',event['message'])
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })

    async def websocket_disconnect(self,event):
        print('Disconnected',event)
        print('Channel Layer...',self.channel_layer)
        print('Channel Layer...',self.channel_name)
        #removing channel from group when connection is lost
        await self.channel_layer.group_discard('group_name',self.channel_name)
        raise StopConsumer()


class MyWebsocketConsumer(WebsocketConsumer):

    def connect(self):
        print('Websocket Connected..')
        self.accept()
        print('Connection Accepted...')

    def receive(self,text_data=None, bytes_data=None):
        print('Data From Client...', text_data)
        self.send(text_data="This is data from server")


    def disconnect(self, code):
        print('Websocket Disconnected...')


class MyAsyncWebsocketConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print('Websocket Connected..')
        print('Channel Name:-',self.channel_layer)
        print('Channel Name:-',self.channel_name)

        print("***********************************")
        print(self.scope['url_route']['kwargs'])
        print("***********************************")
        await self.accept()
        print('Connection Accepted...')

    async def receive(self,text_data=None, bytes_data=None):
        print('Data From Client...', text_data)
        for i in range(5):
            await self.send(text_data=f'This is from AsyncWebsocket Consumer {i}')
        asyncio.sleep(1)

    async def disconnect(self, code):
        print('Websocket Disconnected...',code)


class MyJsonWebSocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        print('Websocket Connected')
        self.accept()
        print('Connection Accepted')

        # This is used for rejecting connection forcefully 
        # self.close()
        # print('Connection Rejected forcefully')

    def receive_json(self, content):
        print('data receive from client',content)
        for i in range(5):
            self.send_json({'content':f"This is data from server {i}"})
        sleep(1)

    def disconnect(self, code):
        print('Websocket disconnected',code)

class MyAsyncJsonWebSocketConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        print('Websocket Connected')

        await self.accept()
        print('Connection Accepted')

    async def receive_json(self, content):
        print('Data received from client',content)

        for i in range(5):
            await self.send_json({'content':f'This is Data from Server {i}'})
        asyncio.sleep(1)

    async def disconnect(self, code):
        print('Websocket disconnected...')