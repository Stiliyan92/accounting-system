import pika
import sys

import settings as s
from common.connector import AMQPConnector

class LogSender(AMQPConnector):

    def __init__(self, server, port, virt_host, credentials, routing_key):
        super(LogSender, self).__init__(server, port, virt_host, credentials)
        self.routing_key = routing_key

    def send_log(self, log):
        self.open_connection()
        self.create_exchange(s.EXCHANGE_NAME, s.EXCHANGE_TYPE)
        self.channel.basic_publish(exchange=self.exchange_name,
                                   routing_key=self.routing_key,
                                   body=log)
        print(" [x] Sent %r:%r" % (self.routing_key, log))
        self.connection.close()
