import os

#dictionary of all environment variables
var = os.environ

#print dictionary
for key, value in var.items():
    print(f'{key}: {value}')
