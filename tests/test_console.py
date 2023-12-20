import unittest
from models.base_model import BaseModel
from models.__init__ import storage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestParamsCreate(unittest.TestCase):
    def setUp(self):
        """ params test """
        self.console = HBNBCommand()
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        """ teardown test """
        self.patcher.stop()

    def test_create_with_params(self):
        """ Test create command with parameters. """
        with patch('sys.stdin', StringIO('create State name="California"\n'
                   'create Place city_id="0001" user_id="0001" '
                   'name="My_little_house" number_rooms=4 '
                   'number_bathrooms=2 max_guest=10 price_by_night=30'
                   'latitude=37.773972 longitude=-122.431297\n'
                   'all State\n'
                   'all Place\n'
                   'quit\n')):
            self.console.cmdloop()

            output = self.mock_stdout.getvalue()
            expected_output = ('(hbnb) d80e0344-63eb-434a-b1e0-07783522124e\n'
                               '(hbnb) 092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7\n'
                               '[[State] (d80e0344-63eb-434a-b1e0-07783522124e) '
                               "{'id': 'd80e0344-63eb-434a-b1e0-07783522124e', "
                               "'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842160), "
                                "'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842235), "
                                "'name': 'California'}, "
                                '[State] (092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7) '
                                "{'id': '092c9e5d-6cc0-4eec-aab9-3c1d79cfc2d7', "
                                 "'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842779), "
                                 "'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 842792), "
                                 "'name': 'Arizona'}]\n"
                                 '(hbnb) (hbnb) 76b65327-9e94-4632-b688-aaa22ab8a124\n'
                                 '[[Place] (76b65327-9e94-4632-b688-aaa22ab8a124) '
                                 "{'number_bathrooms': 2, 'longitude': -122.431297, "
                                 "'city_id': '0001', 'user_id': '0001', 'latitude': 37.773972, "
                                  "'price_by_night': 300, 'name': 'My little house', "
                                  "'id': '76b65327-9e94-4632-b688-aaa22ab8a124', 'max_guest': 10, "
                                  "'number_rooms': 4, 'updated_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843774), "
                                  "'created_at': datetime.datetime(2017, 11, 10, 4, 41, 7, 843747)}]\n"
                                  '(hbnb) \n')
            self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
