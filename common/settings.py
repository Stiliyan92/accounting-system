from config_parser import MyConfigParser

PROJECT_DIR = '/home/sstoyanov/python2016/project16/accounting-system/'
COMMON_DIR = 'common/'
CLIENT_DIR = 'client/'
SERVER_DIR = 'server/'
HPC_INFO = "HPC CENTRE INFORMATION"
JOB_INFO = "JOB INFO"
SETTINGS_INFO = 'APPLICATION SETTINGS'
conf_parser = MyConfigParser()
LOGS_DIR = conf_parser.config_section_map(SETTINGS_INFO)['logsdir']
EXCHANGE_NAME = 'direct_logs'
EXCHANGE_TYPE = 'direct'
CONFIG_PATH = "../accounting.conf"

