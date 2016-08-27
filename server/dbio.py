import MySQLdb
import settings as s


def parse_data(log, table):
    """ Parses log input in appropriate string for inserting
        test_accounting database"""
    date = log.get('log_date')
    datetime = date[6:10] + '-' + date[3:5] + '-' + date[0:2] + date[10:]
    sql_query = "INSERT INTO {} VALUES('{}', '{}', '{}', '{}', \
                 {}, {}, {}, {}, {}, '{}', '{}', '{}')"
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

    def __init__(self, server, database):
        self.server = server
        self.connection = MySQLdb.connect(host='localhost',
                                          user=s.DB_USER,
                                          passwd=s.DB_PASS,
                                          db=database)

    def __enter__(self):
        return self

    def insert_to(self, table, log):
        with self.connection.cursor() as cursor:
            sql_query = parse_data(log, table)
            cursor.execute(sql_query)
        self.connection.commit()
        print("SUCCESS!!!")

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.close()
