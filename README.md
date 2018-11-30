# MMFinder
train a girl classifier based on facial recognition.

## STATUS
Building...

## Building Prerequisite
python3.6 + mongodb

## Crawler Steps
### 1. run the crawler
``` sh
cd crawler
python image_crawler.py
python image_filter.py
```

### 2. face selection
```sh
cd face_selection
python main.py
```
open the http://localhost:3389 , pick up the girls you like.<br>
![face_selection](./face_selection/screenshot.png)

Notice: The more girls you judge, the more accurate it will be.

## Train Steps
### 1. Download Pretrained weights
Google Drive：https://drive.google.com/file/d/1CPSeum3HpopfomUEK1gybeuIVoeJT_Eo/view?usp=sharing]

### 2. Extract Features and Build Dataset

### 3. Train the model

### 4. Use the model

## Reference
- https://sefiks.com/2018/08/06/deep-face-recognition-with-keras/

## LICENSE
MIT
