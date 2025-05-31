from timeit import default_timer as timer
from datetime import datetime
from abc import ABC, abstractmethod
import traceback
import functools


class AbstractorClass:
    def __init__(self):
        pass
    
    @abstractmethod
    def Addition(self):
        pass
    
    @abstractmethod
    def Multiplication(self):
        pass

    @abstractmethod
    def Subtraction(self):
        pass

    @abstractmethod
    def Divition(self):
        pass

class MainCalcluationExceptionError(Exception):
    def __init__(self, message:str):
        super().__init(message)
        print(f"Main Calculation Exception Error: {message}")

class Calculator(AbstractorClass):

    def __init__(self) -> None:
        super().__init__()
        self._value1 = float(input("Enter a Value 1 = "))
        self._value2 = float(input("Enter a Value 2 = "))

    def Addition(self) -> float:
        """
        :Docs Add two values given by user
        :param value_1, value_2 as int or float
        :returns value add by value_1 and value_2
        """
        return self._value1 + self._value2
    
    def Multiplication(self) -> float:
        """
        :Docs Multiply two values given by user
        :param value_1, value_2 as int or float
        :returns value add by value_1 and value_2
        """
        return self._value1 * self._value2
    
    def Subtraction(self) -> float:
        """
        :Docs Subtract two values given by user
        :param value_1, value_2 as int or float
        :returns value add by value_1 and value_2
        """
        return self._value1 - self._value2
    
    def Division(self) -> float:
        """
        :Docs Divide two values given by user
        :param value_1, value_2 as int or float
        :returns value add by value_1 and value_2
        """
        try:
            return self._value1 / self._value2
        except ZeroDivisionError as err:
            print(f"Zero can't be divieded: {err}")
            print("===================Traceback start============================")
            print(traceback.format_exc())
            print("===================Traceback End==============================")
    

def execution_time_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        total_time = (end_time - start_time)
        print(f"Total program Execution Time: {total_time} Seconds")
        return result
    return wrapper

if __name__ == "__main__":

    @execution_time_decorator
    def calculator_executor():
        """Calling Calculator"""
        try:
            obj: Calculator = Calculator()
            print(f"Addition of {obj._value1} + {obj._value2} = {obj.Addition()}")
            print(f"Multiplication of {obj._value1} * {obj._value2} = {obj.Multiplication()}")
            print(f"Subtraction of {obj._value1} - {obj._value2} = {obj.Subtraction()}")
            print(f"Division of {obj._value1} / {obj._value2} = {obj.Division()}")
        except MainCalcluationExceptionError as err:
            raise err
    
    calculator_executor()
