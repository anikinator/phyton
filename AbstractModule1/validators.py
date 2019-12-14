from abc import ABC, abstractmethod, abstractproperty

class AbstractValidator(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def is_valid(self,value=None):
        pass


class TextValidator(AbstractValidator):
    def __init__(self, min_length = 16, max_length = 256):
        self.min_length = min_length
        self.max_length = max_length

    def is_valid(self, value):
        validate_length = len(value)
        if validate_length >= self.min_length and validate_length <= self.max_length:
            return True
        else:
            return False


class IntegerValidator(AbstractValidator):
    def __init__(self, min_value = 32, max_value = 1024):
        self.min_value = min_value
        self.max_value = max_value

    def is_valid(self, value):
        if value >= self.min_value and value <= self.max_value:
            return True
        else:
            return False