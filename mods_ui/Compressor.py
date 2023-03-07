import torch
import torch.nn as nn
import itertools
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

dim = 1
x_min = 0
x_max = 5
x = torch.unsqueeze(torch.arange(x_min, x_max, 0.5), -1)

print(x.shape)

class Func(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.c = nn.Linear(dim, dim)
        #return
    def forward(self, x):
        return self.c(x)

hat_y = Func()
out = hat_y(x)

plt.plot(x.detach().numpy().flatten(), out.detach().numpy().flatten())
plt.show

