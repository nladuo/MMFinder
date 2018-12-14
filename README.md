# MMFinder
训练一个符合自己审美的美眉识别器。

## Status
Building...

## 环境
python3.6 + mongodb

## 数据构建步骤
### 1. 爬取数据
爬取MM图片数据，并筛选出带脸的图片来。
```bash
cd crawler
python image_crawler.py
python image_filter.py
```

### 2. 人工标注
通过以下命令，运行标注前端。
```bash
cd face_selection
python main.py
```
运行后打开[http://localhost:3389](http://localhost:3389), 标注你喜欢的女孩.<br>
![face_selection](./face_selection/screenshot.png)


## 训练步骤
### 1. 下载VGG预训练模型
Google Drive：https://drive.google.com/file/d/1CPSeum3HpopfomUEK1gybeuIVoeJT_Eo/view?usp=sharing]
<br>
百度云链接:https://pan.baidu.com/s/1Dk40tW2lx1ezTda9IyIO9g  密码:0vc7
### 2. 使用VGG提取特征并构建数据集

### 3. 训练数据


## Reference
- https://sefiks.com/2018/08/06/deep-face-recognition-with-keras/

## LICENSE
MIT
