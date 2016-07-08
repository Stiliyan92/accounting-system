import pika
import sys
import os

PROJECT_DIR = '/home/sstoyanov/python2016/project16/accounting-system/'
COMMON_DIR = 'common/'

module_path = os.path.abspath(os.path.join(PROJECT_DIR + COMMON_DIR))
if module_path not in sys.path:
    sys.path.append(module_path)
from connector import AMQPConnector

import settings as s


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
