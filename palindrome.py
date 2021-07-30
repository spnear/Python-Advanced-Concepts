#Programa simple para identificar un palíndromo.

#Revisaremos el tipado estático haciendo uso de mypy:
# $ mypy palindrome.py --check-untyped-defs

def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]


def run():
    print(is_palindrome(1000))


if __name__ == '__main__':
    run()