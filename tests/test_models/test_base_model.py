#!/usr/bin/python3
"""Define test for base model"""
from models.base_model import BaseModel
from datetime import datetime
import unittest
import pep8
from uuid import uuid4
import re
import models
import time


class TestBaseModel(unittest.TestCase):
    """
    Test cases class
    """
    @classmethod
    def setUpClass(cls):
        """Test setUpclass"""
        cls.b = BaseModel()

    def test_check_pep8(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "Solving pep8")

    def test_base_instance(self):
        """b is an instance of BaseModel"""
        self.assertIsInstance(self.b, BaseModel)

    def test_attributes(self):
        """Tests Public Attributes of BaseModel instances"""
        self.assertIsInstance(self.b.id, str)
        self.assertIsInstance(self.b.created_at, datetime)
        self.assertIsInstance(self.b.updated_at, datetime)
        self.assertEqual(str(self.b.created_at).split('.')[0],
                         str(self.b.updated_at).split('.')[0])

    def test_Not_None(self):
        """check existence of docstring in BaseModel functions"""
        b = BaseModel()
        self.assertIsNotNone(b.__doc__)
        self.assertIsNotNone(b.save.__doc__)
        self.assertIsNotNone(b.to_dict.__doc__)

    def test_create_BaseModel_from_dictionary_as_kwargs_valid_attrs(self):
        """ Test cases for instantiation from kwargs """
        id = str(uuid4())
        now = datetime.now().isoformat()
        my_dict = {
            'id': id,
            '__class__': 'dict',
            'created_at': now,
            'updated_at': now
        }
        b = BaseModel(**my_dict)

        self.assertEqual(b.id, id)
        self.assertIs(b.__class__, BaseModel)
        self.assertEqual(now, b.created_at.isoformat())
        self.assertEqual(now, b.updated_at.isoformat())

    def test_more_attributes(self):
        """check if attributes exists"""
        b = BaseModel()
        self.assertTrue(hasattr(b, "__init__"))
        self.assertTrue(hasattr(b, "save"))
        self.assertTrue(hasattr(b, "to_dict"))

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    def test_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_init(self):
        """check if an instance was created upon initialization"""
        self.assertTrue(isinstance(self.b, BaseModel))

    def test_kwargs(self):
        """Kwargs input on BaseModel instantiation"""
        b_dict = self.b.to_dict()
        b2 = BaseModel(**b_dict)
        b2_dict = b2.to_dict()
        self.assertEqual(
            b2_dict['updated_at'].split('T')[0], str(
                self.b.updated_at).split()[0])
        self.assertEqual(
            b2_dict['created_at'].split('T')[1], str(
                self.b.created_at).split()[1])
        self.assertEqual(b2_dict['id'], self.b.id)
        self.assertEqual(b2_dict['__class__'], type(self.b).__name__)

    def test_save(self):
        """check save function of BaseModel"""
        b1 = BaseModel()
        b1.save()
        self.assertNotEqual(b1.created_at, b1.updated_at)

    def test_errs(self):
        """More or less inputs when calling specific base methods"""
        b1 = BaseModel()
        with self.assertRaises(TypeError):
            b2 = BaseModel("I'm not a kwarge")
            b1.save("help")
            b1.to_dict("I'm not a kwarg")
            print(b1.save)

    def test_string_and_dict_and_storage_base_model(self):
        """
            Correct output for a printout usage of __str__
        """
        b1 = BaseModel()
        b1.number = 89
        b1.float_num = 89.9

        # checking if __str__ works by converting it to a string, regex
        string_output = b1.__str__()

        # Correct class
        string_model = re.findall("\\[([^[\\]]*)\\]", string_output)
        self.assertEqual('BaseModel', string_model[0])

        # Correct ID
        string_id = re.findall("\\(.*?\\)", string_output)
        self.assertEqual(string_id[0][1:-1], b1.id)

        # checking if to_dict works with correct values
        b1_dict = b1.to_dict()
        self.assertEqual(b1_dict['__class__'], 'BaseModel')
        self.assertEqual(b1_dict['id'], b1.id)
        updated_at_list = b1_dict['updated_at'].split('T')
        self.assertEqual(" ".join(updated_at_list), str(b1.updated_at))
        created_at_list = b1_dict['created_at'].split('T')
        self.assertEqual(" ".join(created_at_list), str(b1.created_at))
        self.assertEqual(b1_dict['number'], 89)
        self.assertEqual(b1_dict['float_num'], 89.9)

        # checking if to_dict assigns correct values
        self.assertIsInstance(b1_dict, dict)
        self.assertIsInstance(b1_dict['__class__'], str)
        self.assertIsInstance(b1_dict['updated_at'], str)
        self.assertIsInstance(b1_dict['created_at'], str)
        self.assertIsInstance(b1_dict['id'], str)
        self.assertIsInstance(b1_dict['number'], int)
        self.assertIsInstance(b1_dict['float_num'], float)

    def test_datetime_attributes(self):
        """Test that two BaseModel instances have different datetime objects
        and that upon creation have identical updated_at and created_at
        value."""
        tic = datetime.now()
        inst1 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        inst2 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst2.created_at <= toc)
        self.assertEqual(inst1.created_at, inst1.updated_at)
        self.assertEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

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

if __name__ == '__main__':
    unittest.main()
