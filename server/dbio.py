import MySQLdb
import settings as s


def parse_data(log, table):
    """ Parses log input in appropriate string for inserting
        test_accounting database"""
    date = log.get('log_date')
    datetime = date[6:10] + '-' + date[3:5] + '-' + date[0:2] + date[10:]
    sql_query = "INSERT INTO {} VALUES('{}', '{}', '{}', '{}'," + \
                " {}, {}, {}, {}, {}, '{}', '{}', '{}')"
    sql_query = sql_query.format(table, log['server'], log['user'],
                                 log['group'], log['queue'],
                                 log['Resource_List.neednodes'],
                                 log['start'], log['end'],
                                 log['resources_used.mem'][:-2],
                                 log['resources_used.vmem'][:-2],
                                 log['resources_used.cput'],
                                 log['Resource_List.walltime'], datetime)
    return sql_query


class MySQLWrapper():

    s.SERVER = 'localhost'

    def __init__(self, server, database):
        self.server = server
        self.connection = MySQLdb.connect(host=s.SERVER,
                                          user=s.DB_USER,
                                          passwd=s.DB_PASS,
                                          db=database)

    def __enter__(self):
        return self

    def _commit_transaction(self, query):
        success = False
        with self.connection.cursor() as self.cursor:
            self.cursor.execute(query)
            success = True
        self.connection.commit()
        return success

    def insert_to(self, table, log):
        sql_query = parse_data(log, table)
        if self._commit_transaction(sql_query):
            print("SUCCESS!!!")

    def select_entries_by_server(self, server_name):
        sql_query = "SELECT * FROM {} WHERE server = '{}'"
        if self._commit_transaction(sql_query.format(s.TABLE, server_name)):
            return self.cursor

    def select_entries_by_queue(self, queue_name):
        sql_query = "SELECT * FROM {} WHERE queue = '{}'"
        if self._commit_transaction(sql_query.format(s.TABLE, queue_name)):
            return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
