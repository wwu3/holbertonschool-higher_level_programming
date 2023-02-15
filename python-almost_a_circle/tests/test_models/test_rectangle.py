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

if __name__ == "__main__":
    unittest.main()
