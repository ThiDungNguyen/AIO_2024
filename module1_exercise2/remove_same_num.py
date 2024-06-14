def function_helper(x, data):
    if x in data:
        return 0
    else:
        return 1


def my_function(data):
    res = []
    for i in data:
        if function_helper(i, res) == 1:
            res.append(i)
    return res


if __name__ == "__main__":
    lst = [10, 10, 9, 7, 7]
    assert my_function(lst) == [10, 9, 7]

    lst = [9, 9, 8, 1, 1]
    print(my_function(lst))
