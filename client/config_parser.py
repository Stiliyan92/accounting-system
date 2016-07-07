import configparser

CONFIG_PATH = "./accounting.conf"
HPC_INFO = "HPC CENTRE INFORMATION"
JOB_INFO = "JOB INFO"

config = configparser.ConfigParser() 
config.read(CONFIG_PATH)

def config_section_map(section):
    dict1 = {}
    options = config.options(section)
    print(options)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1
#getint(section, option)
#getboolean(section, option)

name = config_section_map(HPC_INFO)['name']
queue = config_section_map(JOB_INFO)['queues']
print(type(queue))
