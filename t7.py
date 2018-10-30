import os
def find(path, filename):
    file = os.listdir(path)
    for i in file:
        if os.path.isdir(path + '\\' + i):
            find(path + '\\' + i, filename)
        else:
            if i == filename:
                print(os.path.basename(path))
                find("C:\\Users\\Vasilija\\PycharmProjects", "task1.py")