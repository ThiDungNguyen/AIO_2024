def check_the_number(N):
    "for question 5"
    list_of_numbers = []
    result = ""
    for i in range(1, 5):
        list_of_numbers.append(i)
    if N in list_of_numbers:
        result = "True"
    if N not in list_of_numbers:
        result = "False"
    return result


if __name__ == "__main__":
    N = 7
    assert check_the_number(N) == "False"
    N = 2
    result = check_the_number(N)
    print(result)
