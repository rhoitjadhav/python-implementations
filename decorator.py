def zero_div_error(func):
    def wrapper(num1, num2):
        if num2 == 0:
            print(f"Cannot divide {num1} from 0")
            return
        return func(num1, num2)

    return wrapper


# With Decorator
@zero_div_error
def divide(a, b):
    print(a / b)


divide(1, 0)

# Without Decorator
wrapper_ = zero_div_error(divide)
wrapper_(1, 1)

