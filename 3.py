import os
import shutil
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

    tmppath = ''
    tmppath = os.path.join(os.getcwd(), path[0])
    fd = [fd.name for fd in os.scandir(tmppath)]

    for i in path[1]:
        if i not in fd:

            os.mkdir(os.path.join(tmppath, i))

    for i in path[2]:
        if i not in fd:

            with open(os.path.join(tmppath, i), 'w') as f:
                f.write('')

p1 = [item for item in os.walk(os.getcwd() + '/my_project')]

for path in p1:

    tmppath = ''
    tmppath = os.path.join(os.getcwd(), path[0])
    fd = [fd.name for fd in os.scandir(tmppath)]
    copypath = os.path.join(os.getcwd(), 'my_project/templates')
    if ('index.html' or 'base.html') in fd:

        tmppathlist = tmppath.split('\\')

        copypath = os.path.join(os.getcwd(), 'my_project/templates' + '/' + tmppathlist[len(tmppathlist) - 1])
        try:
            shutil.copytree(tmppath, copypath)
        finally:
            continue



