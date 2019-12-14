from random import randint
from unittest import TestCase

from tests.utils import gen_random_text
from validators import TextValidator


class TestDefaultTextValidator(TestCase):
    def setUp(self) -> None:
        self.min_length = 16
        self.max_length = 256
        self.validator = TextValidator()

    def test_valid(self):
        num_chars = randint(self.min_length, self.max_length)
        valid_text = gen_random_text(num_chars)
        self.assertTrue(self.validator.is_valid(valid_text))

    def test_invalid_min(self):
        num_chars = randint(-999, 15)
        valid_text = gen_random_text(num_chars)
        self.assertFalse(self.validator.is_valid(valid_text))

    def test_invalid_max(self):
        num_chars = randint(257, 999)
        valid_text = gen_random_text(num_chars)
        self.assertFalse(self.validator.is_valid(valid_text))

    def test_absolute_min_valid(self):
        valid_text = gen_random_text(self.min_length)
        self.assertTrue(self.validator.is_valid(valid_text))

    def test_absolute_max_valid(self):
        valid_text = gen_random_text(self.max_length)
        self.assertTrue(self.validator.is_valid(valid_text))


class TestCustomTextValidator(TestDefaultTextValidator):
    def setUp(self) -> None:
        minimal = randint(0, 128)
        maximal = randint(128, 256)
        self.min_length = minimal
        self.max_length = maximal
        self.validator = TextValidator(min_length=minimal, max_length=maximal)
