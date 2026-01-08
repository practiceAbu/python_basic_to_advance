import random 
from datetime import datetime 
import os
random_number = random.randint(1,20)
print(f'Random number {random_number}')
current_time = datetime.now()
print(f'Current time {datetime}')
current_pwd = os.getcwd()
print(f'Current Directry {current_pwd}')