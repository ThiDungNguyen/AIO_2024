## question 1:

def classifition_f1_score(tp, fp, fn):
    for x in (tp, fp, fn):
       if not isinstance(x,int):
          print(f'input {x} must be int')
          sys.exit()
    for x in (tp, fp, fn):
        if float(x) < 0:
           print(f'input {x} must greater than zero')
           sys.exit()	
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*((precision*recall)/(precision+recall))
    return f1_score
##question2: Viết function mô phỏng theo 3 activation function.
def is_number(x):
    try:
        float(x)
        # Type-casting the string to ‘float‘. # If string is not a valid ‘float‘,
        # it’ll raise ‘ValueError ‘ exception
    except ValueError:
       return False
    return True
def activation_function(x, function, alpha =2):
    if is_number(x) == False:
        print(f'input {x} must be a number, not string')
        sys.exit()
    x = float(x)
    function = str(function)
    if function == 'sigmoid':
        result = 1/(1+math.exp(x))
    elif function == 'relu':
        result = x if x >0 else 0
    elif function == 'elu':
        result = x if x>0 else alpha*(math.exp(x)-1)
    else:
        print(f'{function} is not supportted')
        sys.exit()
    return result
#question 3: 3. Viết function lựa chọn regression loss function để tính loss:
def is_int(x):
    try:
        int(x)
        # Type-casting the string to ‘float‘. # If string is not a valid ‘float‘,
        # it’ll raise ‘ValueError ‘ exception
    except ValueError:
       return False
    return True

def regression_loss_function():
    num_samples = input(f'nhập số lượng sample:')
    y_predict = []
    y_true = []
    if is_int(num_samples) ==  False:
        print(f'input {num_samples} must be a int')
        sys.exit()
    for i in range(int(num_samples)):
        y_predict.append(random.uniform(0,10))
        y_true.append(random.uniform(0,10))
    loss_name = input('Input loss Function (MAE | MSE | RMSE):')
    if loss_name == 'MAE':
        mae = sum(abs(y_p - y_t) for y_p, y_t in zip(y_predict, y_true))/int(num_samples)
        print(f'mae: {mae}') 
    elif loss_name == 'MSE':
        mse = sum((y_p - y_t)**2 for y_p, y_t in zip(y_predict, y_true))/int(num_samples)
        print(f'mse: {mse}')
    elif loss_name == 'MRSE':
        rmse = math.sqrt(sum((y_p - y_t)**2 for y_p, y_t in zip(y_predict, y_true))/int(num_samples))
        print(f'rmse: {rmse}')
    else:
        print(f'{loss_name} is not supportted')
        sys.exit()

### question 4. Viết 4 functions để ước lượng các hàm số sau.

def factorial(x):
    if x == 0:
        return 1
    elif x> 0: 
        fac = 1
        for i in range(1,x +1):
            fac = fac*i
        return fac
    else:
        print(f'{x} must be greater than 0')
        sys.exit()
    
def approx_sin(x,n):
    sin_x = sum(((-1)**i)*(x**(2*i+1))/factorial(2*i+1) for i in range(n)) 
    return sin_x 
def approx_cos(x,n):
     cos_x = sum(((-1)**i)*(x**(2*i))/factorial(2*i) for i in range(n))
     return cos_x
def approx_sinh(x,n):
     sinh_x = sum((x**(2*i+1))/factorial(2*i+1) for i in range(n))
     return sinh_x
def approx_cosh(x,n):
     cosh_x = sum((x**(2*i))/factorial(2*i) for i in range(n))
     return cosh_x

###question 5. Viết function thực hiện Mean Difference of nth Root Error
'''là một kỹ thuật thông dụng trong các ứng dụng như phát hiện và theo dõi đối tượng. Ngoài ra, phương pháp này cũng có thể được áp dụng cho các bài toán hồi quy khác. '''
def md_nre_single_sample(y, y_hat, n, p):
    return  (y**(1/n) - y_hat**(1/n))**p


import sys, math, random
classifition_f1_score(1, 3, 2)
activation_function()
regression_loss_function()
approx_cosh(x=3.14, n=10)
md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1) 

## trắc nghiệm: 
;assert round(classifition_f1_score(tp=2, fp=3, fn=5), 2) == 0.33 
;print(round(classifition_f1_score(tp=2, fp=4, fn=5), 2))

assert is_number (3) == 1.0 
assert is_number('-2a') == 0.0 
print(is_number(1)) 
print(is_number('n'))

assert round(activation_function(3,'sigmoid'), 2)==0.95 
print(round(activation_function(2,'sigmoid'), 2))

assert round(activation_function(1,'elu'))==1 
print(round(activation_function(-1,'elu', alpha = 0.01), 2))

print( activation_function(1, 'relu') )
print(round(activation_function(3, 'sigmoid'), 2))

assert round(approx_cos(x=1, n=10), 2)==0.54 
print(round(approx_cos(x=3.14, n=10), 2))

assert round(approx_sin(x=1, n=10), 4)==0.8415 
print(round(approx_sin(x=3.14, n=10), 4))

assert round(approx_sinh(x=1, n=10), 2)==1.18 
print(round(approx_sinh(x=3.14, n=10), 2))

assert round(approx_cosh(x=1, n=10), 2)==1.54 
print(round(approx_cosh(x=3.14, n=10), 2))
