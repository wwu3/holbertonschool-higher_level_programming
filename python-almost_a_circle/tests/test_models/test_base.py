import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_no_parameters(self):
        b = Base()
        self.assertEqual(b.id, 1)
