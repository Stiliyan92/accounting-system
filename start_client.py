from client.send_logs import send_logs
from common.config_parser import MyConfigParser
import settings as s
import sys

print(sys.path)

conf_parser = MyConfigParser(s.CONFIG_PATH)
s.LOGS_DIR = conf_parser.config_section_map(s.SETTINGS_INFO)['logs_dir']
s.HOST = conf_parser.config_section_map(s.HPC_INFO)['name']
send_logs()
