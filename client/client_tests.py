import unittest
from config_parser import config_section_map

HPC_INFO = "HPC CENTRE INFORMATION"
JOB_INFO = "JOB INFO"
#SETTINGS_INFO = 'APPLICATION SETTINGS'

class TestConfig(unittest.TestCase):

    def test_server_name_if_avitohol(self):
        expected = 'Avitohol'
        self.assertEqual(expected, config_section_map(HPC_INFO)['name'])

    def test_server_country_if_bg(self):
        expected = 'Bulgaria'
        self.assertEqual(expected, config_section_map(HPC_INFO)['country'])

    def test_server_if_viseem(self):
        expected = 'viseem'
        self.assertEqual(expected, config_section_map(JOB_INFO)['groups'])


class TestSendLogs(unittest.TestCase):
    
    def test

if __name__ == '__main__':
    unittest.main()
