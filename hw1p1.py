#!/usr/bin/env python
#import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from IPython.display import Image
list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]

for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))
  
import person
#dictionary people
people={}
for i in range(len(list_of_names)):
    name = list_of_names[i]
    print(name)
    people[name] = person.Person(name, list_of_ages[i], list_of_heights_cm[i])
#dictionary 

my_names_array = np.array(list_of_names)
# printing my_name_array
print(my_names_array)
my_names_array = np.array(list_of_names)
print(my_names_array)
my_ages_array = np.array(list_of_ages)
# printing my_ages_array
print(my_ages_array)
my_heights_array = np.array(list_of_heights_cm)
# printing my_height_array
print(my_heights_array)

#using numpy function to average of the people in the list
my_ages_mean = np.mean(list_of_ages)
print(my_ages_mean)
print(f"Average age of people in list {my_ages_mean} years")

#use matplotlib to create a scatter plot of ages 
plt.plot(list_of_ages,list_of_heights_cm, 'b.')
plt.grid(True)
plt.title("Height (cm) vs Age")
plt.xlabel("Age")
plt.ylabel("Height (cm)")
#saving .png file
plt.savefig('plot1.png', dpi=300, bbox_inches='tight')
plt.show()
