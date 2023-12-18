import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestCreateCommand(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Set up the HBNBCommand instance for testing """
        cls.console = HBNBCommand()

    def setUp(self):
        """ Reset the console and prepare for capturing stdout """
        self.mock_stdout = StringIO()

    def tearDown(self):
        """ Reset the console and close the captured stdout """
        self.mock_stdout.close()

    def test_create_basic_instance(self):
        """ Test creating a basic instance without parameters """
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd('create BaseModel')
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

            obj_id = output
            obj = self.console.classes.get('BaseModel')()
            obj = obj.__dict__.get(obj_id)

    def test_create_instance_with_params(self):
        """ Test creating an instance with parameters """
        with patch('sys.stdout', new_callable=StringIO) as self.mock_stdout:
            self.console.onecmd("create BaseModel name=\"Test\"")
            obj_id = self.mock_stdout.getvalue().strip()
            obj = storage.all().get('BaseModel.{}'.format(obj_id))
            self.assertIsNotNone(obj)
            self.assertEqual(obj.name, "Test")

    def test_create_instance_with_invalid_params(self):
        """ Test creating an instance with invalid parameters """
        with patch('sys.stdout', new=self.mock_stdout):
            self.console.onecmd('create BaseModel invalid_param="Test"')
            output = self.mock_stdout.getvalue().strip()
            self.assertTrue(output)

            obj_id = output
            obj = self.console.classes.get('BaseModel')()
            obj = obj.__dict__.get(obj_id)
            self.assertFalse(hasattr(obj, 'invalid_param'))

    def test_create_insttance_with_qouted_string(self):
        """ Test creating an instance wih a qouted string parameter """
        with patch('sys.stdout', new_callable=StringIO) as self.mock_stdout:
            self.console.onecmd("create Place name=\"My_little_house\"")
            obj_id = self.mock_stdout.getvalue().strip()
            obj = storage.all().get('Place.{}'.format(obj_id))
            self.assertIsNotNone(obj)
            self.assertEqual(obj.name, "My little house")


if __name__ == '__main__':
    unittest.main()
