# base class for all operations
class Operation:
    def calculate(self, first_num, second_num):
        raise NotImplementedError("Must implement calculate")

# addition operation
class Addition(Operation):
    def calculate(self, first_num, second_num):
        return first_num + second_num
# subtraction operation
class Subtraction(Operation):
    def calculate(self, first_num, second_num):
        return first_num - second_num
# multiplication operation
class Multiplication(Operation):
    def calculate(self, first_num, second_num):
        return first_num * second_num
# division operation
class Division(Operation):
    def calculate(self, first_num, second_num):
        if second_num == 0:
            raise ZeroDivisionError("Can't divide by zero")
        return first_num / second_num
