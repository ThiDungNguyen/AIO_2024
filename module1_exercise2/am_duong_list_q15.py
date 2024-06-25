def t_or_n_decision(x):
    'for q15'
    # Your code here
    # Neu x >0 tra ve ’T ’, nguoc lai tra ve ’N’
    if x > 0:
        return 'T'
    else:
        return 'N'


def am_duong_list(data):
    res = [t_or_n_decision(x) for x in data]
    return res


if __name__ == "__main__":

    data = [10, 0, -10, -1]
    assert am_duong_list(data) == ['T', 'N', 'N', 'N']

    data = [2, 3, 5, -1]
    print(am_duong_list(data))
