# TDT4265 Final Project Report
*Kasper Midttun Søreide* <br>

This is a short report of the technical details of the final project in TDT4265

## Hyperparameters
All hyperparameters can be found in the file data/hyp.rdd2022.yaml

## Step guide for how to train the model
1. Install project dependencies:
```
pip install -r requirements.txt
```
2. copy the RDD2022 dataset for Norway into the folder data/RDD2022 and convert annotations to yolo labels by running the code below. This also splits the training data into training and validation.
```
python ./scripts/get_rdd2022_norway.py
```
3. Download pre-trained yolov7-tiny model
```
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-tiny.pt
```
4. Run the training bash script
```
bash ./train_rdd2022.sh
```

## Description of model
The final model can be found in cfg/training/rdd2022-tiny.yaml. It is based on the model in cfg/training/yolov7-tiny.yaml, only difference is number of classes is set to 4. This enabled the use of a pretrained model.

## Training Data
To get both training and validation data, the python script for annotation also splits the training data in 2. Every other image in the training folder is put into the validation folder in the target directory in data/RDD2022/Norway_split. 

