def factorial(y):
    var = 1
    while (y > 1):
        # Your code here
        var = var*y
        y -= 1
    return var


if __name__ == "__main__":
    assert factorial(8) == 40320
    print(factorial(4))
