import torch
import torch.nn as nn
import torch.optim as optim

# Oddiy neyron tarmoq
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Model va optimizer
model = Net()
optimizer = optim.Adam(model.parameters())
