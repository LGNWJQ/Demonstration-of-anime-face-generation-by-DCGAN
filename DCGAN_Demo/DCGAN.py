import random
import torch.nn as nn
import torch.utils.data

import torchvision.utils as vutils
import numpy as np
import matplotlib.pyplot as plt

# 设置随机种子
manualSeed = random.randint(1, 10000)
print("Random Seed: {}".format(manualSeed))
random.seed(manualSeed)
torch.manual_seed(manualSeed)

# 定义生成器类
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()

        self.main = nn.Sequential(
            # 输入通道100, 输出ngf*8通道
            nn.ConvTranspose2d(100, 64 * 8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(64 * 8),
            nn.ReLU(True),
            # 当前尺寸： (ngf*8) x 4 x 4
            nn.ConvTranspose2d(64 * 8, 64 * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(64 * 4),
            nn.ReLU(True),
            # 当前尺寸： (ngf*4) x 8 x 8
            nn.ConvTranspose2d(64 * 4, 64 * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(64 * 2),
            nn.ReLU(True),
            # 当前尺寸： (ngf*2) x 16 x 16
            nn.ConvTranspose2d(64 * 2, 64, 4, 2, 1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU(True),
            # 当前尺寸： (ngf) x 32 x 32
            nn.ConvTranspose2d(64, 3, 4, 2, 1, bias=False),
            nn.Tanh()
            # 当前尺寸： (nc=3) x 64 x 64
        )

    def forward(self, input):
        return self.main(input)

# 获取设备，优先GPU，其次CPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# 权重文件路径，更改来使用不同的文件
Generator_Path = "Generator_100.pth"
img_num = 64

# 构造生成器对象
Gn = Generator()
Gn = Gn.cuda()
# 导入权重文件
Gn.load_state_dict(torch.load(Generator_Path))

# 生成随机潜向量
noise = torch.randn(img_num, 100, 1, 1, device=device)
# 使用生成器将潜向量转化为图像
fake = Gn(noise).detach().cpu()
img = vutils.make_grid(fake, padding=2, normalize=True)

# 绘制图像
plt.axis("off")
plt.imshow(np.transpose(img, (1, 2, 0)))
plt.savefig("Random Seed={}.jpg".format(manualSeed))
plt.show()
