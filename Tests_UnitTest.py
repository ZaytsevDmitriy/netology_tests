import unittest
import app
from unittest.mock import patch

class TestSecretaryProgram(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    @patch('app.input')
    def test_get_doc_owner_name(self, mock_input):
        mock_input.return_value = '10006'
        self.assertEqual(app.get_doc_owner_name(), 'Аристарх Павлов')

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)

    @patch('app.input')
    def test_add_new_shelf(self,mock_input):
        mock_input.return_value = '5'
        self.assertEqual(app.add_new_shelf(), ('5', True))

    @patch('app.input')
    def test_move_doc_to_shelf(self, mock_input):
        mock_input.side_effect = [app.documents[1]['number'], '1']
        app.move_doc_to_shelf()
        self.assertIn(app.documents[1]['number'], app.directories['1'])

    def tearDown(self):
        print('method tearDown')
