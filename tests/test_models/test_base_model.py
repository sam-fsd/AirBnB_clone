#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import unittest
import models
import inspect
module_doc = models.base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                )
                self.assertTrue(
                    len(func[1].__doc__) > 1,
                    "{:s} method needs a docstring".format(func[0])
                )


class TestBasemodel(unittest.TestCase):

    def test_id_type(self):
        """test if attribute is string"""
        bmodel = BaseModel()
        self.assertTrue(isinstance(bmodel.id, str))

    def test_uuid(self):
        """Test that id is a valid uuid"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

    def test_created_at(self):
        """test if attribute is of datetime object"""
        bmodel = BaseModel()
        self.assertTrue(isinstance(bmodel.created_at, datetime))
        self.assertTrue(isinstance(bmodel.created_at.isoformat(), str))

    def test_updated_at(self):
        """test if attribute is of datetime object"""
        bmodel = BaseModel()
        self.assertTrue(isinstance(bmodel.updated_at, datetime))
        self.assertTrue(isinstance(bmodel.updated_at.isoformat(), str))

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))
    
    def test_instantiation_with_kwargs(self):
        """Test object instantion with kwargs"""
        d = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                'created_at': '2017-09-28T21:03:54.052298',
                '__class__': 'BaseModel',
                'my_number': 89,
                'updated_at': '2017-09-28T21:03:54.052302',
                'name': 'My_First_Model'
            }
        b = BaseModel(**d)
        
        self.assertEqual(b.id, d['id'])
        self.assertTrue(isinstance(b.created_at, datetime))
        self.assertTrue(isinstance(b.updated_at, datetime))
        
    def test_to_dict(self):
        """Test for to_dict() method"""
        b = BaseModel()

        self.assertTrue(isinstance(b.to_dict(), dict))
