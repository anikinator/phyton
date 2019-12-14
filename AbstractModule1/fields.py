from abc import ABC, abstractmethod, abstractproperty
from validators import TextValidator, IntegerValidator

class AbstractField(ABC):
    @abstractmethod
    def __init__(self, validators=None):
        pass

    @abstractmethod
    def is_valid(self,value=None):
        pass


class CharField(AbstractField):
    def __init__(self, validators=None):
        self.default_validators = [TextValidator(min_length=0, max_length=999)]
        self.all_validators = self.default_validators
        if isinstance(validators,list) and validators:
            self.all_validators = self.default_validators + validators

    def is_valid(self,value):
        return all(validator.is_valid(value) for validator in self.all_validators)

class TextField(AbstractField):
    def __init__(self, validators=None):
        self.default_validators = [TextValidator(min_length=1001, max_length=3000)]
        self.all_validators = self.default_validators
        if isinstance(validators,list) and validators:
            self.all_validators = self.default_validators + validators

    def is_valid(self,value):
        return all(validator.is_valid(value) for validator in self.all_validators)

class IntegerField(AbstractField):
    def __init__(self, validators=None):
        self.default_validators = [IntegerValidator(min_value=128, max_value=1024)]
        self.all_validators = self.default_validators
        if isinstance(validators,list) and validators:
            self.all_validators = self.default_validators + validators

    def is_valid(self,value):
        return all(validator.is_valid(value) for validator in self.all_validators)