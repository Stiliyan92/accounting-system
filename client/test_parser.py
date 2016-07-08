import unittest
from LogParser import LogParser

class TestConfig(unittest.TestCase):

    def setUp(self):
        """ Setting up for the test """
        self.log_parser = LogParser('./')
        self.log_parser.parse_pbs('pbs_test_log')
        self.logs = self.log_parser.get_logs()

    def test_if_user_is_pesho(self):
        expected = 'pesho'
        self.assertEqual(expected, self.logs[0]['user'])

    def test_if_group_is_hakeri(self):
        expected = 'hakeri'
        self.assertEqual(expected, self.logs[0]['group'])

    def test_if_jobname_is_test(self):
        expected = 'test'
        self.assertEqual(expected, self.logs[0]['jobname'])

    def test_exit_status(self):
        expected = '-9999'
        self.assertEqual(expected, self.logs[0]['Exit_status'])

    def test_cpu_usage(self):
        expected = '99:99:99'
        self.assertEqual(expected, self.logs[0]['resources_used.cput'])

    def test_virt_memory_used(self):
        expected = '20kb'
        self.assertEqual(expected, self.logs[0]['resources_used.vmem'])



if __name__ == '__main__':

    unittest.main()
