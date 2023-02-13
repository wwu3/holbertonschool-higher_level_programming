import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):

    def test_idf(self):
        Base.__nb_objects = 0
        r = Rectangle(1, 2)
        self.assertEqual(r.id, 1)

