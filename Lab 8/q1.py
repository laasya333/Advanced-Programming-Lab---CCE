import re

functions = [func for func in dir(re) if 'find' in func]

functions.sort()

print("Function names containing 'find' in the re")
for func in functions:
    print(func)
