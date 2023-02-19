import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def test_idf(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.id, Base.get_nb_objects())
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.area(), 2)

    def test_not_negative(self):
        with self.assertRaises(Exception) as context:
            Rectangle(-1, 0)

    def test_width_string(self):
        with self.assertRaises(Exception) as context:
            Rectangle("2", 3)

    def test_height_string(self):
        with self.assertRaises(Exception) as context:
            Rectangle(2, "3")

    def test_width_negative(self):
        with self.assertRaises(Exception) as context:
            Rectangle(-2, 3)

    def test_height_negative(self):
        with self.assertRaises(Exception) as context:
            Rectangle(2, -3)

    def test_width_zero(self):
        with self.assertRaises(Exception) as context:
            Rectangle(0, 3)
   
    def test_height_zero(self):
        with self.assertRaises(Exception) as context:
            Rectangle(2, 0)

if __name__ == "__main__":
    unittest.main()
