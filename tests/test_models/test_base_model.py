#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBasemodel(unittest.TestCase):

    def test_id_type(self):
        bmodel = BaseModel()
        self.assertTrue(isinstance(bmodel.id, str))
    def test_uuid(self):
        bmodel = BaseModel()
        self.assertTrue(isinstance(bmodel.created_at, datetime))
if __name__ == "__main__":
    unittest.main()
