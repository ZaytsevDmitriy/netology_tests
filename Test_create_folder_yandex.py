import unittest
import create_folder_yandex
import requests


class Test_create_folder_yandex(unittest.TestCase):

    def setUp(self):
        print('method setUp')

    def test_create_folder(self):
        self.assertEqual(create_folder_yandex.create_folder('some_folder_name'), 201)

    def tearDown(self):
        print('method tearDown')