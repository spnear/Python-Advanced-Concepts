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


#Decoradores que reciben argumentos de entrada
#Simplemente hay que anidar otra función en el decorador

def with_custom_message(message):
    def with_message(func):
        print(f'{message}:')
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper
    return with_message

@with_custom_message('Hello')
def multiply(a,b):
    print(f"the result of {a} * {b} is {a*b}")

if __name__ == '__main__':

    hello()
    #Out:
    # -> Added this to original func
    # -> Hello!
    print(message('Juan'))

    multiply(10,2)

