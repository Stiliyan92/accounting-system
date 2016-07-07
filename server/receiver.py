from connector import AMQPConnector
import pika

class Receiver(AMQPConnector):

def __init__(self, server, port=5672, virt_host='/', credentials, routing_key):
        super(LogReceiver, self).__init__(server, port, virt_host, credentials)
        self.routing_key = routing_key


    def callback(self, ch, method, properties, body):
        log = json.loads(body.decode())
            for key, value in log.items():
            output = "{0} : {1]".format(key,value)
            print(output)

            
    def create_queue(self):
        self.queue = channel.queue_declare()
        self.queue_name = self.queue.method.queue


    def bind_queue(self):
        self.channel.queue_bind(exchange=self.exchange_name,
                                queue=queue_name,
                                self.routing_key)

    

