import pika
import json

class AMQPConnector():

    def __init__(self, server, port, virt_host, credentials):
        self.server = server
        self.port = port
        self.virt_host = virt_host
        self.user = pika.PlainCredentials('test', 'test')

    def open_connection(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(self.server, self.port,
                                      self.virt_host, self.user))
        self.create_channel()


    def create_channel(self):
        self.channel = self.connection.channel()

    def create_exchange(self, exchange_name, exchange_type):
        self.exchange_name, self.exchange_type = exchange_name, exchange_type
        self.channel.exchange_declare(exchange=self.exchange_name,
                         type=self.exchange_type)

