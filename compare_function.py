def compare_function(alist, number=1):
    '''any(# Your code here : Thuc hien duyet tung phan tu trong integers , so sanh
tung phan tu voi number , neu bang nhau tra ve True , khac nhau tra ve false
 #vi du: integers = [1 , 2 , 3] , number = 2 , ban se tao ra list [False ,
rue , False ] )'''
    result = []
    for i in alist:
        if i != number:
            result.append(False)
        else:
            result.append(True)
    return any(result)


if __name__ == "__main__":
    my_list = [1, 3, 9, 4]
    assert compare_function(my_list, -1) == False

    my_list = [1, 2, 3, 4]
    print(compare_function(my_list, 2))
