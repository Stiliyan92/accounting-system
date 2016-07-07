from LogParser import LogParser
from sender import LogSender
import json

log_parser = LogParser('../')
log_parser.parse_pbs("pbs_log")
logs = log_parser.get_logs()
HOST, VIRT_HOST, CREDENTIALS  = '194.141.225.78', '/', ('test', 'apredatorr')
PORT, ROUTING_KEY = 5672, 'logs'
server = LogSender(HOST, PORT, VIRT_HOST, CREDENTIALS, ROUTING_KEY) 
for log in logs:
    body=json.dumps(log)
    server.send_log(body)
