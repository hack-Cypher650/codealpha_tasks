import os
import shutil
path = input('Enter the source path: ')
op= input('New dest folder? (y/n)')
if op=='y':
    z = input('Enter the path of the directory in which the folder will be created: ')
    x = input('Enter folder name: ')
    path2 = os.path.join(z,x)
    mode = 0o666
    os.mkdir(path2, mode)
else:
    path2= input('Enter Dest folder path: ')
dir_list = os.listdir(path)
for i in dir_list:
    if '.jpg' in i:
        p=os.path.join(path, i)
        print(shutil.copy(p,path2), end='\n')
        os.remove(p)
