from LogParser import LogParser
from sender import LogSender
import json
import os, sys

PROJECT_DIR = '/home/sstoyanov/python2016/project16/accounting-system/'
COMMON_DIR = 'common/'

module_path = os.path.abspath(os.path.join(PROJECT_DIR + COMMON_DIR))
if module_path not in sys.path:
    sys.path.append(module_path)

import settings as s

log_parser = LogParser(s.LOGS_DIR)
log_parser.parse_pbs("pbs_log")
logs = log_parser.get_logs()
HOST, VIRT_HOST, CREDENTIALS  = '194.141.225.78', '/', ('test', 'apredatorr')
PORT, ROUTING_KEY = 5672, 'logs'
server = LogSender(HOST, PORT, VIRT_HOST, CREDENTIALS, ROUTING_KEY) 
for log in logs:
    body=json.dumps(log)
    server.send_log(body)
