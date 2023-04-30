#!/bin/sh

python train.py --workers 8 --device 0 --batch-size 16 --data data/rdd2022.yaml --img 1024 512 --cfg cfg/training/rdd2022-tiny.yaml --weights 'yolov7-tiny.pt' --name rdd2022-tiny-transfer --hyp data/hyp.rdd2022.yaml --epochs 50 | tee ./log.txt