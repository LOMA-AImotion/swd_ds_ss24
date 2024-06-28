"""
Definiert eine Funktion, die eine Liste von Werten aufsummiert
"""
def sum_of_list(values):
    s = 0
    for i in values:
        s += i
    return s

# packe den Test in eine Main-Funktion
if __name__ == "__main__":
    print(sum_of_list([1, 3, 5]))
