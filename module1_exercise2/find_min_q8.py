def find_min(alist):
    "for question 8"
    # Your code here
    min_ = min(alist)
    return min_


if __name__ == "__main__":
    my_list = [1, 22, 93, -100]
    assert find_min(my_list) == -100

    my_list = [1, 2, 3, -1]
    print(find_min(my_list))
