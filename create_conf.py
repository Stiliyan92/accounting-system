import configparser
import settings as s

Config = configparser.ConfigParser()
# lets create that config file for next time...
cfgfile = open(s.PROJECT_DIR + "accounting.conf",'w')

# add the settings to the structure of the file, and lets write it out...
Config.add_section('HPC CENTRE INFORMATION')
Config.set('HPC CENTRE INFORMATION','Name','Avitohol')
Config.set('HPC CENTRE INFORMATION','Country', 'Bulgaria')


Config.add_section('JOB INFO')
Config.set('JOB INFO','Queues','')
Config.set('JOB INFO','Groups', 'viseem')

Config.add_section('PROGRAM SETTINGS')
Config.set('PROGRAM SETTINGS','Logs_Dir',
           '/home/stiliyan/python/')

Config.write(cfgfile)
cfgfile.close()
