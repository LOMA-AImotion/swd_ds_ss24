"""
Definiert eine Funktion, die eine Liste von Werten aufsummiert
"""
from numbers import Number

def sum_of_list(values : list) -> Number:
    return sum(values)

# packe den Test in eine Main-Funktion
if __name__ == "__main__":
    print(sum_of_list([1, 3, 5]))
