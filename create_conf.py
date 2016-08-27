import configparser
import settings as s

Config = configparser.ConfigParser()
cfgfile = open(s.PROJECT_DIR + "accounting.conf",'w')

Config.add_section(s.HPC_INFO)
Config.set(s.HPC_INFO,'Name','Avitohol')
Config.set(s.HPC_INFO,'Country', 'Bulgaria')

Config.add_section(s.JOB_INFO)
Config.set(s.JOBINFO,'Queues','')
Config.set(JOB_INFO,'Groups', 'viseem')

Config.add_section(s.SETTINGS_INFO)
Config.set(s.SETTINGS_INFO,'Logs_Dir',
           '/home/stiliyan/python/')

Config.write(cfgfile)
cfgfile.close()
