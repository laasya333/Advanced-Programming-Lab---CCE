import datetime

def greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if 3 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 16:
        return "Good afternoon!"
    else:
        return "Good evening!"


name = input("Enter name: ")

def greettime():
    message=greeting().split()
    return message[1]
    
greet = greeting()
time = greettime()

print(f"Hello, {name}! {greet}")
print(f"Have a great {time}!")
