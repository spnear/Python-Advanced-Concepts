#Validar eficiencia del programa calculando tiempos de ejecucion

from datetime import datetime

#*args, **kwargs para enviar n cantidad de parametros

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"It took {time_elapsed.total_seconds()} seconds")
    return wrapper


#Probando decorador
@execution_time
def random_func():
    for _ in range(1,1000000):
        pass


@execution_time
def add(a: int,b: int) ->int:
    return a+b


@execution_time
def hello(name = 'Juan'):
    print(f"Hello {name}")

if __name__ == '__main__':
    print("Test 1")
    random_func()

    print("Test 2")
    add(2,10)

    print("Test 3")
    hello()
    hello("Sebastian")
