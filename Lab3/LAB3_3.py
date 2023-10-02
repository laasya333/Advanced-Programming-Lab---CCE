def funct():
    a = 766
    b = "abc"
    c = [1,2,3]
    d = (2,3,4)

def count_local_variables(func):
    num = func.__code__.co_nlocals
    return num


count = count_local_variables(funct)
print(f"Number of local variables in funct: {count}")
