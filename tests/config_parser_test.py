import unittest
import settings as s
from common.config_parser import MyConfigParser


class TestImages(unittest.TestCase):

    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        self.conf_parser = MyConfigParser('./tests/example.conf')

    def tearDown(self):
        pass

    def test_server_name_if_avitohol(self):
        expected = 'Spam'
        result = self.conf_parser.config_section_map(s.HPC_INFO)['name']
        self.assertEqual(expected, result)

    def test_server_country_if_bg(self):
        expected = 'Bacon'
        result = self.conf_parser.config_section_map(s.HPC_INFO)['country']
        self.assertEqual(expected, result)

    def test_server_if_viseem(self):
        expected = 'Eggs'
        result = self.conf_parser.config_section_map(s.JOB_INFO)['groups']
        self.assertEqual(expected, result)

    def test_log_dir(self):
        expected = '/home/sstoyanov/python2016/pbs_logs/'
        result = self.conf_parser.config_section_map(s.SETTINGS_INFO)['logs']
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
