
import torch
import torch.nn as nn

# for question 1:
data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)
assert round(output[0].item(), 2) == 0.09

print(output)

# q2,3:


class MySoftmax (nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        # Your Code Here
        softmax_function = nn.Softmax(dim=0)
        output = softmax_function(data)
        return output
        # End Code Here


data = torch.Tensor([5, 2, 4])
my_softmax = MySoftmax()
output1 = my_softmax(data)
assert round(output1[-1].item(), 2) == 0.26
print('output1: ', output1)


data = torch . Tensor([1, 2, 300000000])
my_softmax = MySoftmax()
output2 = my_softmax(data)
assert round(output2[0]. item(), 2) == 0.0
print('output2: ', output2)
