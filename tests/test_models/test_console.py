import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from datetime import datetime


class TestConsoleCreateCommand(unittest.TestCase):
     
    def setUp(self):
         self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create_valid_instance(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd('create BaseModel name="test" number_rooms=3')
            result = mock_stdout.getvalue().strip()
            self.assertTrue(result.startswith("[BaseModel]")

    def test_create_with_parameters(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd('create BaseModel name="test" number_rooms=3')
            result = mock_stdout.getvalue().strip()
            self.assertTrue(result.startswith("[BaseModel]"))

    @classmethod
    def tearDownClass(cls):
    pass

if __name__ == '__main__:
    unittest.main()
