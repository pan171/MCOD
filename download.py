from torchvision.datasets import FashionMNIST
from torchvision.datasets import STL10

data_dir = 'stl10_data/'
img_train_data = STL10(root=data_dir, split='train', download=True)
img_test_data = STL10(root=data_dir, split='test', download=True)

# data_dir = 'fashion_mnist_data/'
# img_train_data = FashionMNIST(root=data_dir, train=True, download=True)
# img_test_data = FashionMNIST(root=data_dir, train=False, download=True)

# nohup python download.py > down.log 2>&1 &