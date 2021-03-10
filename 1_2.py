import os
print(os.getcwd())

# paths = [
#     ('', ['my_project'], []),
#     ('my_project', ['settings', 'mainapp', 'adminapp', 'authapp'], [])
# ]
paths = []
with open('config.yaml', 'r') as f:
    for i in f:
        paths.append(eval(i.strip()))
#print(paths)
#print(type(eval("('', ['my_project'], [])")))

for path in paths:

    #print(path)
    tmppath = ''
    tmppath = os.path.join(os.getcwd(), path[0])
    #print(tmppath)
    fd = [fd.name for fd in os.scandir(tmppath)]
    #print(fd)

    for i in path[1]:
        if i not in fd:

            os.mkdir(os.path.join(tmppath, i))

    for i in path[2]:
        if i not in fd:

            with open(os.path.join(tmppath, i), 'w') as f:
                f.write('')

p1 = [item for item in os.walk(os.getcwd())]
print(p1)
