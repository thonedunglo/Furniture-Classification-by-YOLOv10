import os
from ultralytics import YOLOv10
os.environ["WANDB_MODE"] = "disabled"
%cd '/content/drive/MyDrive/YOLOv10'
!yolo task=detect mode=train epochs=50 batch=32 plots=True model='./pretrain/yolov10n.pt' data='/content/drive/MyDrive/YOLOv10/train_data/data.yaml'