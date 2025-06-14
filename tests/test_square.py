import unittest
from square import app, square_number

class TestSquareFunction(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(square_number(5), 25)

    def test_zero(self):
        self.assertEqual(square_number(0), 0)

    def test_negative(self):
        self.assertEqual(square_number(-3), 9)

    def test_float(self):
        self.assertAlmostEqual(square_number(2.5), 6.25)

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_request(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Number", response.data)

    def test_post_valid_number(self):
        response = self.client.post("/", data={"number": "4"})
        self.assertIn(b"Result", response.data)
        self.assertIn(b"16", response.data)

    def test_post_invalid_input(self):
        response = self.client.post("/", data={"number": "abc"})
        self.assertIn(b"Invalid input", response.data)

if __name__ == "__main__":
    unittest.main()
