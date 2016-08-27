import json
#import os
#import sys
from client.log_parser import LogParser
from client.sender import LogSender

#PROJECT_DIR = '/home/sstoyanov/python2016/project16/accounting-system/'
#COMMON_DIR = 'common/'

#module_path = os.path.abspath(os.path.join(PROJECT_DIR + COMMON_DIR))
#if module_path not in sys.path:
#    sys.path.append(module_path)
import settings as s

def send_logs():
    log_parser = LogParser(s.LOGS_DIR)
    log_parser.parse_pbs("pbs_log")
    logs = log_parser.get_logs()
#    HOST, VIRT_HOST, CREDENTIALS = '194.141.225.78', '/', ('test', 'apredatorr')
#    PORT, ROUTING_KEY = 5672, 'logs'
    server = LogSender(s.SERVER, s.PORT, s.VIRT_HOST, s.CREDENTIALS, s.ROUTING_KEY)
    for log in logs:
        body = json.dumps(log)
        server.send_log(body)
