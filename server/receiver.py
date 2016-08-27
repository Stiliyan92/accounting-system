from common.connector import AMQPConnector
import pika
import json
import settings as s
from server.dbio import MySQLWrapper

class LogReceiver(AMQPConnector):

    def __init__(self, server, port, virt_host, credentials, routing_key):
        super(LogReceiver, self).__init__(server, port, virt_host, credentials)
        self.routing_key = routing_key

    def callback(self, ch, method, properties, body):
        log = json.loads(body.decode())
        if log:
            with MySQLWrapper(s.SERVER, s.DATABASE) as sql_conn:
                sql_conn.insert_to(s.TABLE, log)

    def receive_logs(self):
        self.open_connection()
        self.create_exchange(s.EXCHANGE_NAME, s.EXCHANGE_TYPE)
        self.create_queue()
        self.bind_queue()
        self.channel.basic_consume(self.callback, queue=self.queue_name, no_ack=True)
        print(' [*] Waiting for logs. To exit press CTRL+C')
        self.channel.start_consuming()


    def create_queue(self):
        self.queue = self.channel.queue_declare()
        self.queue_name = self.queue.method.queue


    def bind_queue(self):
        self.channel.queue_bind(exchange=self.exchange_name,
                                queue=self.queue_name,
                                routing_key=self.routing_key)
