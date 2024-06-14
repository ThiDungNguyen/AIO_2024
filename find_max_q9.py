def find_max(alist):
    "for question 8"
    # Your code here
    max_ = max(alist)
    return max_


if __name__ == "__main__":
    my_list = [1001, 9, 100, 0]
    assert find_max(my_list) == 1001

    my_list = [1, 9, 9, 0]
    print(find_max(my_list))
