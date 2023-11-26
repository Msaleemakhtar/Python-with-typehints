from typing import Callable

def my_fun(func: Callable[[int], int]) -> Callable[[int], int]:
    def inner_func(num1: int) -> int:
        print("Something is happening before the callback function")
        result = func(num1)
        print("Something is happening after the callback function")
        return result  # Ensure that inner_func returns an int
    return inner_func

@my_fun
def add(num1: int) -> int:
    sum1 = num1 + 100
    print(f"Num1 is {sum1}")
    return sum1  # Ensure that add returns an int

result = add(300)
print(f"Result is {result}")
