import pika
from receiver import LogReceiver


PORT, ROUTING_KEY = 5672, 'logs'
HOST, VIRT_HOST, CREDENTIALS  = '194.141.225.78', '/', ('admin', 'b3T@_testing')                                                                                                                                   
server = LogReceiver(SERVER, PORT, VIRT_HOST, CREDENTIALS, ROUTING_KEY)
server.receive_logs()

