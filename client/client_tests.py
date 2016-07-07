import unittest

from config_parser import config_section_map


class TestImages(unittest.TestCase):

    HPC_INFO = "HPC CENTRE INFORMATION"

    def test_server_name(self):
        expected = 'Avitohol'
        self.assertEqual(expected, config_section_map(self.HPC_INFO)['name'])

    def test_server_country(self):
        expected = 'Bulgaria'
        self.assertEqual(expected, config_section_map(self.HPC_INFO)['country'])


if __name__ == '__main__':
    unittest.main()
