#!/bin/sh

python test.py --data ./data/rdd2022.yaml --img 1024 --batch 8 --conf 0.001 --iou 0.65 --device 0 --weights ./runs/train/rdd20225/weights/best.pt --name rdd2022_tiny_val
