import unittest

from config_parser import MyConfigParser


class TestImages(unittest.TestCase):

    HPC_INFO = "HPC CENTRE INFORMATION"
    JOB_INFO = "JOB INFO"

    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        self.conf_parser = MyConfigParser('example.conf')

    def tearDown(self):
        pass

    def test_server_name_if_avitohol(self):
        expected = 'Spam'
        self.assertEqual(expected,
                         self.conf_parser.config_section_map(self.HPC_INFO)['name'])

    def test_server_country_if_bg(self):
        expected = 'Bacon'
        self.assertEqual(expected, 
                         self.conf_parser.config_section_map(self.HPC_INFO)['country'])

    def test_server_if_viseem(self):
        expected = 'Eggs'
        self.assertEqual(expected,
                         self.conf_parser.config_section_map(self.JOB_INFO)['groups'])


if __name__ == '__main__':
    unittest.main()
