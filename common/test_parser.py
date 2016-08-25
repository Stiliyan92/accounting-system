import unittest

from config_parser import MyConfigParser


class TestImages(unittest.TestCase):

    HPC_INFO = "HPC CENTRE INFORMATION"
    JOB_INFO = "JOB INFO"
    SETTINGS_INFO = "APPLICATION SETTINGS"
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        self.conf_parser = MyConfigParser('example.conf')

    def tearDown(self):
        pass

    def test_server_name_if_avitohol(self):
        expected = 'Spam'
        result = self.conf_parser.config_section_map(self.HPC_INFO)['name']
        self.assertEqual(expected, result)

    def test_server_country_if_bg(self):
        expected = 'Bacon'
        result = self.conf_parser.config_section_map(self.HPC_INFO)['country']
        self.assertEqual(expected, result)

    def test_server_if_viseem(self):
        expected = 'Eggs'
        result = self.conf_parser.config_section_map(self.JOB_INFO)['groups']
        self.assertEqual(expected, result)

    def test_log_dir(self):
        expected = '/home/sstoyanov/python2016/pbs_logs/'
        result = self.conf_parser.config_section_map(self.SETTINGS_INFO)['logs']
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
