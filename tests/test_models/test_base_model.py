#!/usr/bin/python3

from models.base_model import BaseModel
from uuid import uuid4
from datetime import datetime
import unittest

"""the Basemodel test cases class base """

class TestBaseModelClass(unittest.TestCase):  
    
      """ the TestIdString function test case
      tests the data type of the id provided by the 
      object
      """

      def testIdIsString(self):
        obj_instance = BaseModel()
        self.assertIsInstance(obj_instance.id, str)


      """ test case to check for the attribute created_at"""

      def test_to_dict_contains_created_at(self):
            obj_instance = BaseModel()
            obj_dict = obj_instance.to_dict()
            self.assertIn('created_at', obj_dict)
            self.assertIsInstance(obj_dict['created_at'], str)

      """ the testcase checks for the attribute updated_at 
      in the object instance 
      """
      def test_to_dict_contains_updated_at(self):
            obj_instance = BaseModel()
            obj_dict = obj_instance.to_dict()
            self.assertIn('updated_at', obj_dict)
            self.assertIsInstance(obj_dict['updated_at'], str)
   

      """ the TestCreatesAsIsDateTime function test case
      checks the value type of datetime
      """ 
      def testCreatedAtIsDatetime(self):
        obj_instance = BaseModel()
        self.assertIsInstance(obj_instance.created_at, datetime)

      """ checks the test case for updated_at function 
      to assertain if the value is datetime
      """   
      def testUpdatedAtIsDatetime(self):
         obj_instance = BaseModel()
         self.assertIsInstance(obj_instance.updated_at, datetime)

      """checks if the new date time has been updated in the 
      updated_at attribute
      """
      def testSaveUpdatedAt(self):
        obj_instance = BaseModel()
        old_updated_at = obj_instance.updated_at
        obj_instance.save()
        new_updated_at = obj_instance.updated_at
        self.assertGreater(new_updated_at, old_updated_at)

      """ The testCase checks if the value returned is a dictionary
      type value from the class instance
      """
      def testDictionaryType(self):
            obj_instance = BaseModel()
            obj_dict = obj_instance.to_dict()
            self.assertIsInstance(obj_dict, dict)

      """ the testcase checks for class name in the 
      object value
      """
      def test_to_dict_contains_class_name(self):
            obj_instance = BaseModel()
            obj_dict = obj_instance.to_dict()
            self.assertIn('__class__', obj_dict)
            self.assertEqual(obj_dict['__class__'], 'BaseModel')

