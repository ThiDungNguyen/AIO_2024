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


if __name__ == "__main__":
    file_path = '/content/P1_data.txt'
    result = count_word(file_path)
    assert result['who'] == 3
    print(result['man'])
