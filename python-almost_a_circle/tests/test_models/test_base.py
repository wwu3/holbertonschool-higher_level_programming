import unittest
from models.base import Base
from models.square import Square


class TestBase(unittest.TestCase):

    def test_no_parameters(self):
        b = Base()
        self.assertEqual(b.id, 1)
    
    def test_parameters(self):
        b = Base(41)
        self.assertEqual(b.id, 41)

    def test_json(self):
        self.assertEquals(Base.to_json_string([{"id": 3}]), '[{"id": 3}]')
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])

    def test_save_and_load_from_file(self):
        #list of squares
        list_of_square = [Square(12), Square(24, 2, 3, 77)]

        #save list to file
        Square.save_to_file(list_of_square)

        #load file to instances
        list_of_objects = Square.load_from_file()

        #compare original assertEquals loaded
        self.assertEquals(list_of_square[0].id, list_of_objects[0].id)
        self.assertEquals(list_of_square[0].width, list_of_objects[0].width)
        self.assertEquals(list_of_square[0].height, list_of_objects[0].height)
        self.assertEquals(list_of_square[0].x, list_of_objects[0].x)
        self.assertEquals(list_of_square[0].y, list_of_objects[0].y)
        self.assertEquals(list_of_square[1].id, list_of_objects[1].id)
        self.assertEquals(list_of_square[1].width, list_of_objects[1].width)
        self.assertEquals(list_of_square[1].height, list_of_objects[1].height)
        self.assertEquals(list_of_square[1].x, list_of_objects[1].x)
        self.assertEquals(list_of_square[1].y, list_of_objects[1].y)

