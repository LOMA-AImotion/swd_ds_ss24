def double_list(values: list) -> list:
    if not isinstance(values, list):
        raise TypeError(f"Expect type list in double_list but got {type(values)}")
    if not all(isinstance(v, (int, float)) for v in values):
        raise ValueError("All elements in the list must be numeric (int or float)")
    return [2*v for v in values]

def quiet_double_list(values):
    try: 
        doubles = double_list(values)
    except Exception as e:
        return None
    
try:
    print(quiet_double_list([1, 5, 7]))
    print(quiet_double_list("Wrong_type"))
    print(quiet_double_list(3.14))
    print("Am I getting here at all?")
except Exception as exception:
    print(type(exception))
    print(exception.args)
    print(exception)