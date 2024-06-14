def chia_het_cho3(data):
    var = []
    for i in data:
        # Your code here
        # Neu i chia het cho 3 thi them i vao list var
        if i % 3 == 0:
            var.append(i)
    return var


if __name__ == "__main__":

    assert chia_het_cho3([3, 9, 4, 5]) == [3, 9]
    print(chia_het_cho3([1, 2, 3, 5, 6]))
