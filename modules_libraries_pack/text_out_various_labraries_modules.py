import math

num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
# gives us remainder of the 2 values
# 5 can't go into 1, so the remainder is
print(f"Remainder from 1/5: {math.remainder(1, 5)}")


import os
# returns our current working directory
working_directory = os.getcwd()
print(f"Current working directory: {working_directory}")

username = os.environ.get('USERNAME') or os.environ.get('USER')
print(f"The current user is: {username}")

cpu_cores = os.cpu_count()
print(f'Total CPU cores: {cpu_cores}')
# change directory - must exist
# os.chdir("<folder_name>")
# make a new directory
#os.mkdir("created_by_python")

import datetime
# gives us today's date
print(f"Today's date: {datetime.date.today()}")
print(f"Today's date: {datetime.datetime.now()}")


import builtins
for name in dir(builtins):
    if name[0].islower():
        print(name)