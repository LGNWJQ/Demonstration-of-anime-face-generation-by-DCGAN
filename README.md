# Demonstration-of-anime-face-generation-by-DCGAN
数字信号处理期末课程设计Topic1图像扩增中的一部分：DCGAN

## 环境

* Python3.7
* PyTorch 1.10.1


## 文件结构

```shell
-> DCGAN_train # 训练相关
	-> data # 数据集根目录
		-> anime-faces
			-> 1.jpg
			-> 2.jpg
			...
	-> DCGAN.ipynb # 训练脚本
	# 训练好的权重，后面的数字表示训练轮数
	-> Discriminator_25.pth
	-> Discriminator_50.pth
	-> Discriminator_100.pth
	-> Generator_25.pth
	-> Generator_50.pth
	-> Generator_100.pth
-> DCGAN_Demo # 利用训练好的权重生成图片
	-> DCGAN.py # 运行该文件可生成图片
	# 不同的生成器权重
	-> Generator_25.pth
	-> Generator_50.pth
	-> Generator_100.pth
	
```

