def double_list(values: list) -> list:
    return [2*v for v in values]

try:
    print(double_list([1, 5, 7]))
    print(double_list("Wrong_type"))
    print(double_list(3.14))
    print("Am I getting here at all?")
except Exception as exception:
    print(type(exception))
    print(exception.args)
    print(exception)