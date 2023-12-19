#!/usr/bin/python3
""" Test for def all in the console """
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsoleCreateCommand(unittest.TestCase):

    def assert_stdout(self, expected_output, input_cmd):
        """  test for asset stddout  """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('sys.stdin', StringIO(input_cmd)):
                HBNBCommand().cmdloop()
                self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create_command_state(self):
        """ test for command state """
        expected_output = "(hbnb) d80e0344-63eb-434a-b1e0-07783522124e\n"
        input_cmd = 'create State name="California"\n'
        self.assert_stdout(expected_output, input_cmd)

    def test_create_command_place(self):
        """ test for create command place """
        expected_output = "(hbnb) 76b65327-9e94-4632-b688-aaa22ab8a124\n"
        input_cmd = 'create Place city_id="0001" user_id="0001"\n' \
                    'name="My_little_house" number_rooms=4 ' \
                    'number_bathrooms=2 max_guest=10 price_by_night=300 ' \
                    'latitude=37.773972 longitude=-122.431297\n'
        self.assert_stdout(expected_output, input_cmd)

    def test_create_command_invalid_parameters(self):
        """ test for create command invalid parameters """
        expected_output = "(hbnb)\n"
        input_cmd = 'create InvalidClassn\n'
        self.assert_stdout(expected_output, input_cmd)


if __name__ == '__main__':
    unittest.main()
