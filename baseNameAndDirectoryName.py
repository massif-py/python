import os

path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.basename(path))
print(os.path.dirname(path))

calcFilePath = path
print(os.path.split(calcFilePath))

print((os.path.dirname(path), os.path.basename(path)))

print(calcFilePath.split(os.sep))
print('/usr/bin'.split('/'))
