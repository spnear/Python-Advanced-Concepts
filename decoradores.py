#Un decorador es un closure especial:
"""
Un decorador es una función que recibe como parámetro otra
función, le añade cosas, la ejecuta y retorna esta función
modificada (diferente)
"""

def decorator(func):
    def wrapper():
        print('Added this to original func')
        func()
    return wrapper

def hello():
    print('Hello!')

if __name__ == '__main__':
    hello()
    #Out: Hello!

    hello = decorator(hello)
    hello()
    #Out:
    # -> Added this to original func
    # -> Hello!