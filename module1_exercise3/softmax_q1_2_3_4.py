
import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        softmax_function = nn.Softmax(dim=0)
        output = softmax_function(data)
        return output


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition


# for question 1:
data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
assert round(output[0].item(), 2)*100 == 9
print(output)

# q2:
data = torch.Tensor([5, 2, 4])
my_softmax = MySoftmax()
output1 = my_softmax(data)
assert round(output1[-1].item(), 2)*100 == 26
print('output1: ', output1)

# q3:
data = torch.Tensor([1, 2, 300000000])
my_softmax = MySoftmax()
output2 = my_softmax(data)
assert round(output2[0]. item(), 2) == 0
print('output2: ', output2)

# q4
data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
assert round(output[-1]. item(), 2)*100 == 67
print(output)
