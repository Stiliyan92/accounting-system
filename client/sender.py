import pika
import sys
from connector import AMQPConnector


class LogSender(AMQPConnector):

    EXCHANGE_NAME = 'direct_logs'
    EXCHANGE_TYPE = 'direct'

    def __init__(self, server, port, virt_host, credentials, routing_key):
        super(LogSender, self).__init__(server, port, virt_host, credentials)
        self.routing_key = routing_key

    def send_log(self, log):
        self.open_connection()
        self.create_exchange(self.EXCHANGE_NAME, self.EXCHANGE_TYPE)
        self.channel.basic_publish(exchange=self.exchange_name,
                      routing_key=self.routing_key,
                      body=log)
        print(" [x] Sent %r:%r" % (self.routing_key, log))
        self.connection.close()
