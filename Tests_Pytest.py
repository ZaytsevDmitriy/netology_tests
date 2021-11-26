import app
from unittest.mock import patch

class Tests_Pytest:

    @classmethod
    def setUp(cls):
        print('method setUp')

    @patch('app.input')
    def test_delete_doc(self, mock_input):
        mock_input.return_value = '10006'
        assert app.delete_doc() == ('10006', True)

    @patch('app.input')
    def test_get_doc_owner_name(self, mock_input):
        mock_input.return_value = '11-2'
        assert app.get_doc_owner_name() == ('Геннадий Покемонов')

    @patch('app.input')
    def test_move_doc_to_shelf(self, mock_input):
        mock_input.side_effect = [app.documents[1]['number'], '3']
        app.move_doc_to_shelf()
        assert app.directories['3'] == ['11-2']

    def test_show_document_info(self):
        app.show_document_info(app.documents[0])
        assert app.documents[0]['type'] == "passport" \
               and app.documents[0]['number'] == '2207 876234'

    @classmethod
    def tearDown(cls):
        print('method tearDown')


