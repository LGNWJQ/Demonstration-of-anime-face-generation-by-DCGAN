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
-> DCGAN_Demo # 利用训练好的权重生成图片
	-> DCGAN.py # 运行该文件可生成图片
	# 不同的生成器权重
	-> Generator_25.pth
	-> Generator_50.pth
	-> Generator_100.pth
	
```
## 注意

在训练时，在该路径下放置要训练的图片

DCGAN_train/data/anime-faces

这里提供数据集下载，下载后解压到上述路径即可开始训练

链接：https://pan.baidu.com/s/1tdxHPkGwKNorxV3T-34V9Q 
提取码：0000
