def average(list_nums=[0, 1, 2]):
    '''# Your code here : Tra ve gia tri trung binh cua list bang cach chia var cho
 luong phan tu trong list_mums'''
    var = 0
    for i in list_nums:
        var += i
    return var/len(list_nums)


if __name__ == "__main__":
    assert average([4, 6, 8]) == 6
    print(average())
