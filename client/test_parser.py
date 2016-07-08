import unittest

from config_parser import config_section_map


class TestImages(unittest.TestCase):

    HPC_INFO = "HPC CENTRE INFORMATION"
    JOB_INFO = "JOB INFO"

    def test_server_name_if_avitohol(self):
        expected = 'Avitohol'
        self.assertEqual(expected, config_section_map(self.HPC_INFO)['name'])

    def test_server_country_if_bg(self):
        expected = 'Bulgaria'
        self.assertEqual(expected, config_section_map(self.HPC_INFO)['country'])

    def test_server_if_viseem(self):
        expected = 'viseem'
        self.assertEqual(expected, config_section_map(self.JOB_INFO)['groups'])


if __name__ == '__main__':
    unittest.main()
