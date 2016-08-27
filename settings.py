import os

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__)) + '/'
COMMON_DIR = 'common/'
CLIENT_DIR = 'client/'
SERVER_DIR = 'server/'
HPC_INFO = "HPC CENTRE INFORMATION"
JOB_INFO = "JOB INFO"
SETTINGS_INFO = 'PROGRAM SETTINGS'
CONFIG_PATH = "./accounting.conf"
EXCHANGE_NAME = 'direct_logs'
EXCHANGE_TYPE = 'direct'
HOST = '194.141.225.78'
SERVER = HOST
DATABASE = 'test_accounting'
TABLE = 'log'
DB_USER = 'root'
DB_PASS = 'b3T@_testing'
VIRT_HOST = '/'
CREDENTIALS = ('test', 'b3T@_testing')
ADMIN = ('admin', 'b3T@_testing')
PORT = 5672
ROUTING_KEY = 'logs'
