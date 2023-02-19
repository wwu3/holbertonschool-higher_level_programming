import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_no_parameters(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_json(self):
        self.assertEquals(Base.to_json_string([{"id": 3}]), '[{"id": 3}]')
        self.assertNotEqual(Base.from_json_string('[{ "id": 89 }]'), '[{ "id": 89 }]')
        self.assertEqual(Base.from_json_string([{"id": 1}]), '[{"id": 15}]')
