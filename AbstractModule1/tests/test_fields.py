from random import randint
from unittest import TestCase

from fields import CharField, TextField, IntegerField
from tests.utils import gen_random_text


class TestCharField(TestCase):
    def setUp(self) -> None:
        self.test_field = CharField()
        self.valid_char_num = randint(0, 1000)
        self.invalid_char_num = randint(1001, 2000)
        self.valid_text = gen_random_text(self.valid_char_num)
        self.invalid_text = gen_random_text(self.invalid_char_num)

    def test_valid_char_field(self):
        self.assertTrue(self.test_field.is_valid(self.valid_text))

    def test_invalid_char_field(self):
        self.assertFalse(self.test_field.is_valid(self.invalid_text))


class TestTextField(TestCase):
    def setUp(self) -> None:
        self.test_field = TextField()
        self.valid_char_num = randint(1001, 3000)
        self.invalid_char_num = randint(0, 999)
        self.valid_text = gen_random_text(self.valid_char_num)
        self.invalid_text = gen_random_text(self.invalid_char_num)

    def test_valid_text_field(self):
        self.assertTrue(self.test_field.is_valid(self.valid_text))

    def test_invalid_text_field(self):
        self.assertFalse(self.test_field.is_valid(self.invalid_text))


class TestIntegerField(TestCase):
    def setUp(self) -> None:
        self.test_field = IntegerField()
        self.valid_int = randint(128, 1024)
        self.invalid_int = randint(1025, 2000)

    def test_valid_integer_field(self):
        self.assertTrue(self.test_field.is_valid(self.valid_int))

    def test_invalid_integer_field(self):
        self.assertFalse(self.test_field.is_valid(self.invalid_int))
