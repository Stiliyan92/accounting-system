from common.config_parser import MyConfigParser
import os

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__)) + '/'
COMMON_DIR = 'common/'
CLIENT_DIR = 'client/'
SERVER_DIR = 'server/'
HPC_INFO = "HPC CENTRE INFORMATION"
JOB_INFO = "JOB INFO"
SETTINGS_INFO = 'PROGRAM SETTINGS'
CONFIG_PATH = "./accounting.conf"
#conf_parser = MyConfigParser(CONFIG_PATH)
#LOGS_DIR = conf_parser.config_section_map(SETTINGS_INFO)['log_dir']
EXCHANGE_NAME = 'direct_logs'
EXCHANGE_TYPE = 'direct'
HOST = '194.141.225.78'
VIRT_HOST = '/'
CREDENTIALS = ('test', 'apredatorr')
PORT = 5672
ROUTING_KEY = 'logs'
