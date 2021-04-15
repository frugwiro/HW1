import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Image
class Person:
  def __init__(self, name, age, height):
    self.name = name
    self.age = age
    self.height = height
  def __repr__(self):
    return "{} is {} year old and {} cm tall" .format(self.name, self.age, self.height)
new_person = Person(name='Joe', age=34, height=184)
print("{:} is {:} year old." .format(new_person.name, new_person.age))
p1 = Person('Joe', 34, 184) 
print(p1) 