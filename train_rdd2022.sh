#!/bin/sh

python train.py --workers 8 --device 0 --batch-size 8 --data data/rdd2022.yaml --img 1024 512 --cfg cfg/training/rdd2022-tiny.yaml --weights '' --name rdd2022 --hyp data/hyp.rdd2022.yaml --epochs 20 | tee ./log.txt