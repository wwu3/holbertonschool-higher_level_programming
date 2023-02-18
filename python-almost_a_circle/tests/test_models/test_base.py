import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_no_parameters(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_json(self):
        b = Base(6)
        self.assertEquals(b.to_json_string(), "{id: gfgidf, age: 66, name: Zoe")
