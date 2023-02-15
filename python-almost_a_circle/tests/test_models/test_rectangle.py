import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def test_idf(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.id, Base.get_nb_objects())

if __name__ == "__main__":
    unittest.main()
