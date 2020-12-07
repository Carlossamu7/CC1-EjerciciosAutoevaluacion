from app import app
import unittest

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hola Mundo!', response.data)

    def test_hello_name(self):
        response = self.app.get('/carlos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hola carlos!', response.data)

if __name__ == '__main__':
    unittest.main()
