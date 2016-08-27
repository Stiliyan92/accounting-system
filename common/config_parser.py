import configparser

CONFIG_PATH = 'accounting.conf'


class MyConfigParser():

    def __init__(self, config_path=CONFIG_PATH):
        self.config = configparser.ConfigParser(allow_no_value=True)
        self.config.read(config_path)

    def config_section_map(self, section):
        """ returns all configuration options in 'section' in a dict with
        key: config_option and value: the read value in the file"""
        dict1 = {}
        options = self.config.options(section)
        for option in options:
            try:
                dict1[option] = self.config.get(section, option)
                if dict1[option] == -1:
                    DebugPrint("skip: %s" % option)
            except:
                dict1[option] = None
        return dict1

# getint(section, option)
# getboolean(section, option)
