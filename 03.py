import os 
directory_path = '/courses'

contents = os.listdir(directory_path)

for item in contents:
    print(item) 