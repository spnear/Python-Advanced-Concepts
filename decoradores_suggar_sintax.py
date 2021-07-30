"""
Versión Pythonic para uso de decoradores
"""

def decorator(func):
    def wrapper():
        print('Added this to original func')
        func()
    return wrapper


@decorator
def hello():
    print('Hello!')



def mayus(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper


@mayus
def message(name):
    return f'{name} you got a message'

if __name__ == '__main__':

    hello()
    #Out:
    # -> Added this to original func
    # -> Hello!
    print(message('Juan'))