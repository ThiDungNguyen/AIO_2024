# phan I. Câu hỏi tự luận

# question 1.
'''Cho một list các số nguyên num_list và một sliding window có kích thước size k di
chuyển từ trái sang phải. Mỗi lần dịch chuyển 1 vị trí sang phải có thể nhìn thấy
đươc k số trong num_list và tìm số lớn nhất trong k số này sau mỗi lần trượt k phải
lớn hơn hoặc bằng 1'''

import subprocess


def max_kernel(num_list, k):
    result = []
    for i in range(len(num_list)-k+1):
        sublist = num_list[i:(i+k)]
        print(max(sublist))
        result.append(max(sublist))
    return result


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


# question 3:
''' Viết function đọc các câu trong một file txt, đếm số lượng các từ xuất hiện và trả về một dictionary
với key là từ và value là số lần từ đó xuất hiện.'''


def count_word(file_path):
    counter = {}
    file = open(file_path, 'r')
    words_list = file.read().split()
    for w in words_list:
        if w not in counter:
            counter[w] = 1
        else:
            counter[w] += 1
    print(counter)
    return counter


def download_file(url):
    try:
        subprocess.run(['gdown', url], check=True)
        print("File downloaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


# question 4:
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
    # return distance


max_kernel(num_list=[3, 4, 5, 1, -44, 5, 10, 12, 33, 1], k=3)
character_count('Happiness')
download_file(
    'https://drive.google.com/uc?id =1IBScGdW2xlNsc9v5zSAya548kNgiOrko')
count_word('file_for_module1_hw2')
levenshtein_distance('yo', 'you')

phan 2 trac nghiem
assert max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_kernel(num_list, k))

assert character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
print(character_count('smiles'))

levenshtein_distance("hi", " hello ")
levenshtein_distance(" hola ", " hello ")
