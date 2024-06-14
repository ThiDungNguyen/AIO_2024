# Question 2:
'''Viết function trả về một dictionary đếm số lượng chữ xuất hiện trong một từ, với key là chữ cái
và value là số lần xuất hiện'''


def character_count(word):
    character_statistic = {}
    letters = list(word)
    for l in letters:
        if l not in character_statistic.keys():
            character_statistic[l] = 1
        else:
            character_statistic[l] += 1
    print(character_statistic)
    return character_statistic


if __name__ == "__main__":
    assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
    print(character_count('smiles'))
