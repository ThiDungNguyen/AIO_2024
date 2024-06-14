'''Viết chương trình tính khoảng cách chỉnh sửa tối thiểu Levenshtein. Khoảng cách Levenshtein thể
hiện khoảng cách khác biệt giữa 2 chuỗi ký tự.'''


def levenshtein_distance(token1, token2):
    len_1 = len(token1)
    len_2 = len(token2)
    # step 1
    D = [[0 for _ in range(len_2+1)] for _ in range(len_1+1)]
    # step 2
    for i in range(1, len_2+1):
        D[0][i] = i
    for i in range(1, len_1+1):
        D[i][0] = i
    # step 3
    for i in range(1, len_1 + 1):
        for j in range(1, len_2 + 1):
            if token1[i - 1] == token2[j - 1]:
                sub_cost = 0
            else:
                sub_cost = 1
            D[i][j] = min(
                D[i - 1][j] + 1,  # Deletion
                D[i][j - 1] + 1,  # Insertion
                D[i - 1][j - 1] + sub_cost  # Substitution
            )
    print(D)


if __name__ == "__main__":
    assert levenshtein_distance("hi", "hello") == 4
    print(levenshtein_distance("hola", "hello"))
