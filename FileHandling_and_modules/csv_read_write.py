import csv 
file_path = 'data.csv'
data =[
    ['name','age','city'],
    ['Abu',23,'bangaluru'],
    ['Shaba',25,'Chennai'],
    ['Bala',33,'Puna']
]
with open(file_path,'w',newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

with open(file_path,'r',newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader :
     print(i)