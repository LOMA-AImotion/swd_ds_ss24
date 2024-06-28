import logging 

x = 42
y = "7"
#y = 7

logging.basicConfig(level=logging.INFO)

def my_func(x : int) -> int:
    if x < 0: 
        raise RuntimeError("Input cannot be 0 for my_func")
    else:
        return 2*x
try :
    z = x / y
    print(my_func(5))
    print(my_func(-5))
except TypeError as te :
    print(te)
    logging.exception(te)
except RuntimeError: # no info about the actual error is preserved
    print("Oh here we've got another error")
else:
    print("Alles in Ordnung")
finally:
    print("We're doing this ")