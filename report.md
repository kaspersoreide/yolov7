got these results:
```
    Epoch   gpu_mem       box       obj       cls     total    labels  img_size
    35/299     5.35G   0.05399  0.004034  0.006746   0.06477        27       608: 100%|█████████████████████████████████| 241/241 [01:46<00:00,  2.27it/s]
               Class      Images      Labels           P           R      mAP@.5  mAP@.5:.95: 100%|███████████████████████| 45/45 [00:14<00:00,  3.17it/s]
                 all        2829        1745       0.271       0.155     0.00747     0.00191

```
with this yaml file:
```
download: bash ./scripts/get_rdd2022.sh

train: ./data/RDD2022/India/train
test: ./data/RDD2022/Norway/test/images
val: ./data/RDD2022/Czech/train

nc: 4
names: ['D00', 'D10', 'D20', 'D40']
```

log after tiny training
```

                 all        4080        5851    0.000351      0.0076    2.84e-05    4.88e-06
                 all        4080        5851     0.00044      0.0157    4.12e-05    7.05e-06
                 all        4080        5851     0.00139     0.00377    0.000254    6.78e-05
                 all        4080        5851       0.502     0.00467     0.00146    0.000298
                 all        4080        5851       0.754     0.00676     0.00196     0.00112
                 all        4080        5851       0.765      0.0151     0.00405    0.000955
                 all        4080        5851       0.765      0.0126     0.00403     0.00104
                 all        4080        5851       0.768      0.0222     0.00615     0.00141
                 all        4080        5851       0.292      0.0352     0.00758     0.00159
                 all        4080        5851      0.0234      0.0562     0.00728     0.00153
                 all        4080        5851       0.277      0.0527     0.00707     0.00145
                 all        4080        5851       0.539      0.0486      0.0105     0.00275
                 all        4080        5851       0.779      0.0356      0.0118     0.00279
                 all        4080        5851       0.531       0.028      0.0116     0.00261

```
## Step guide for how to train the model
1. First, copy the dataset and convert annotations to yolo labels by running
```
python ./scripts/get_rdd2022.py
```
2. Download pre-trained yolov7 model
```
wget https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt
```
3. Run the training bash script
```
bash ./train_rdd2022.sh
```

## Description of model
The model can be found in cfg/training/yolov7-rdd2022.yaml. It is the same as the original cfg/training/yolov7.yaml except number of classes is set to 4.

