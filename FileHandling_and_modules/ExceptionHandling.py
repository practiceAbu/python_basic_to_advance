file_path = 'file.txt'

try:
    with open(file_path,'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File not found {file_path}")
    