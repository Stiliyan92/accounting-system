class LogEntry():

    PROPERTY = ['server', 'user', 'group', 'queue', 'Resource_List.neednodes',
                'start', 'end', 'resources_used.mem', 'resources_used.vmem',
                'resources_used.cput', 'Resource_List.walltime', 'log_date']

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                if key in self.PROPERTY:
                    setattr(self, key, dictionary[key])
        for key in kwargs:
            if key in self.PROPERTY:
                setattr(self, key, kwargs[key])
