# GIF2Animate

将GIF图像经过处理转换为能让`animate`宏包使用的格式。

## 前提

1. 保证你的Python版本至少为3.6
2. 安装依赖`Pillow`，可使用`requirements.txt`

## 用法

`python3 gif2animate.py file [file ...]`

可以加入多个GIF图像的路径，脚本可以处理多幅图像。

输出的文件均保存在位于图像同路径的同名文件夹中，内含所有帧的静态图片，以及一份时间轴文件。

以下LaTeX代码可以插入这个图像序列：
```latex
\usepackage{animate}
\animategraphics[loop, autoplay, timeline=<时间轴文件>]{<数字随便填>}{<图像序列前缀>}{<首帧编号>}{<尾帧编号>}
```
