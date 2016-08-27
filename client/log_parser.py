import time
from os import listdir
from os.path import isfile, join
import settings as s


class LogParser:
    NOT_NEEDED = ["exec_host", "session", "owner"]

    def __init__(self, logs_dir):
        self.hpc_logs = []
        self.last_log = ''
        self.logs_dir = logs_dir
        # log_files = [f for f in listdir(self.logs_dir)
        # if isfile(join(mypath, f))]

    def process_pbs_line(self, pbs_line):
        timestamp, rec_type, job_id, line_record = pbs_line.split(';', 3)
        parsed_ts = time.strptime(timestamp, "%m/%d/%Y %H:%M:%S")
        dict_of_job_info = {'job_id': job_id, 'server': s.HOST,
                            'log_date': timestamp}
        # if state of job is exited succesfuly
        if rec_type == 'E':
            for item in line_record.split(' '):
                try:
                    # if more than one node there is additional ppn data
                    if 'ppn' in item:
                        for sub_item in item.split(':'):
                            key, value = sub_item.split('=')
                            dict_of_job_info[key] = value
                    else:
                        key, value = item.split('=')
                        if key not in self.NOT_NEEDED:
                            dict_of_job_info[key] = value
                except:
                    break
            return dict_of_job_info
        else:
            return {}

    def parse_pbs(self, file_name):
        with open(self.logs_dir + file_name, "r") as pbs_log:
            self.hpc_logs = [self.process_pbs_line(line) for line in pbs_log]
        self.last_log = file_name

    def get_logs(self):
        return self.hpc_logs
