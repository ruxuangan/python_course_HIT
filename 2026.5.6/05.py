# import random
# win = []
# for i in range(6):
#     win.append(random.randint(1,49))
# print(win)

# from datetime import datetime
# class Person:
#     def __init__(self, name, country, birth_date):
#         self.name = name
#         self.country = country
#         self.birth_date = birth_date

#     def compute_age(self):
#         current_year = datetime.now().year
#         person_year = int(self.birth_date[:4])
#         age = current_year - person_year
#         return age

#     def __str__(self):
#         return f"{self.name} {self.country} {self.birth_date}"

# p1_person =Person("Bob","China","20070503" )

# print(p1_person.compute_age())

import os
print(os.getcwd())

my_file = open( file = "sample.txt" , mode="w")
my_file.write('Hello file!')
my_file.write('\n')
my_file.write('This is me!')
my_file.close()
my_file = open(file='sample.txt', mode='r')
file_output = my_file.readlines()
print(file_output)
my_file.close()