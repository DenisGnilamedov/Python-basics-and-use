# можно наследоваться от класса Exception, чтобы задать, например, свое имя ошибки:
class BadName(Exception):
    pass

def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise ValueError(name + " is inappropriate name") # BadName(name + " is inappropriate name")

while True:
    try:
        name = input("enter your name: ")
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print("Try again")
    else:
        break



