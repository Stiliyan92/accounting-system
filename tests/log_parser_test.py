import unittest
from client.log_parser import LogParser


class TestConfig(unittest.TestCase):

    def setUp(self):
        """ Setting up for the test """
        self.log_parser = LogParser('./tests/')
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

    def test_if_dict_size_is(self):
        expected = 21
        self.assertEqual(expected, len(self.logs[0]))

    def test_exception_if_file_name_error(self):
        self.failed_parser = LogParser('./')
        self.assertRaises(IOError, self.failed_parser.parse_pbs, 'no_such_log')


if __name__ == '__main__':

    unittest.main()
