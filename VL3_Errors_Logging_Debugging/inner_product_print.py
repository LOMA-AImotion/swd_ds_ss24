def inner_product(x:list, y:list) -> int:
    result = 0
    for i in range(len(x)):
        result += x[i]*y[0]
        print(f"After element {i}, result is now {result}")
    return result

def test_inner_product(x:list, y:list, expected:int):
    actual = inner_product(x, y)
    if actual != expected:
        print(f"Error: Inner product of {x} and {y} should be {expected} but is {actual}")

if __name__ == "__main__":
    test_inner_product([1,3,5], [0, 1, -1], -2)