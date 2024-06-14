def reverse_function ( x ) :
    # your code here
    new_x = "" 
    for index, _ in enumerate(x):
        new_x += x[len(x) - index-1]
    return new_x
    

if __name__ == "__main__":
    x = 'I can do it'
    assert reverse_function (x ) =="ti od nac I"
    
    x = 'apricot'
    print ( reverse_function ( x ) )