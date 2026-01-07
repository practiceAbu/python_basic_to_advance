with open('file.txt','r') as file:
    content = file.readlines()
    for i in content:
        print(i.strip())