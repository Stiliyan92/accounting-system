import json
from client.log_parser import LogParser
from client.sender import LogSender
import settings as s

def send_logs():
    log_parser = LogParser(s.LOGS_DIR)
    log_parser.parse_pbs("pbs_log")
    logs = log_parser.get_logs()
    server = LogSender(s.SERVER, s.PORT, s.VIRT_HOST, s.CREDENTIALS, s.ROUTING_KEY)
    for log in logs:
        body = json.dumps(log)
        server.send_log(body)
