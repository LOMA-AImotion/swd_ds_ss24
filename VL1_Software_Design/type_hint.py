def my_func(x: float) -> float:
    if isinstance(x, float):
        return 2.0 * x
    else:
        raise RuntimeError(f"Wrong type, expected float but got {type(x)}")


print(my_func(1.5))
print(my_func("Hallo SWD DS"))