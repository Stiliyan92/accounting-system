import unittest
import server.dbio
import settings as s

class TestConfig(unittest.TestCase):

    def setUp(self):
        """ Setting up for the test """
        self.sql_wrapper = MySQLWrapper(s.SERVER, S.DATABASE)
        self.log_parser.parse_pbs('pbs_test_log')
        self.log_entry = {"resources_used.walltime": "37:49:17\\n",
                          "Exit_status": "0", "Resource_List.nodes": "1",
                          "etime": "1453799100",
                          "resources_used.cput": "37:48:13",
                          "log_date": "01/28/2016 00:54:18",
                          "resources_used.vmem": "3376844kb",
                          "server": "Avitohol", "user": "prdlhcb006",
                          "queue": "lhcb", "start": "1453799101",
                          "jobname": "cream_875940740",
                          "Resource_List.neednodes": "1",
                          "resources_used.mem": "1590068kb",
                          "Resource_List.nodect": "1",
                          "Resource_List.walltime": "72:00:00",
                          "group": "prdlhcb", "qtime": "1453799100",
                          "ctime": "1453799100", "job_id": "1397150.torq.hpcg",
                          "end": "1453935258"}

    def test_if_parsing_correctly_1_node(self):
        expected = "INSERT INTO log VALUES('Avitohol', 'prdlhcb006', 'prdlhcb', \
                    'lhcb', 1, 1453799101, 1453935258, 1590068, 3376844, \
                    '37:48:13', '72:00:00', '2016-28-01 00:54:18')"
        result = parse_data(self.log_entry, s.TABLE)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
