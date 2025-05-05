from datetime import datetime
from typing import Self


'''
def show_date() -> None:
    print('This is the current time: {}'.format(datetime.now()))
#print(datetime.now())
show_date()

def greet(name: str) -> None:
    print(f'Hello, {name}')

greet('Candace')

def add(a: float, b: float) -> float:
    return a+b

print(f'{add(7.2,5.4): .2f}') 

print(f'{add(4.5, 2.3): .2f}')'''


class Students:
    def __init__(self, name: str, gender: str, age: int) -> None:
        self.name = name #class attribute
        self.gender = gender #class attribute
        self.age = age #class attribute

    def __str__(self) -> str:
        return f'{self.name}, {self.gender}, {self.age} old.'
    
    def __add__(self, other: Self) -> str:
        return f'{self.name} & {other.name}'
    
    def info(self) -> None: #Class method
        return f'{self.name} is {self.gender} and {self.age} years old.'

    def activity(self) -> None: #Class method
        return f'{self.name} is studying.'




student_1: Students  = Students('Angela', 'Female', 22)
student_2: Students = Students('Mark', 'Male', 20)

print(student_1 + student_2)
print(student_1.info())
print(student_1.activity())
print(student_2.info())
print(student_2.activity())


