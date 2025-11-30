# train.py

import torch
from ultralytics import YOLO
import multiprocessing

def train():
    # 1. Cihaz kontrolü
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"[INFO] Training on {device}")

    # 2. Modeli başlat (yolov8n: hızlı, mobil uyumlu)
    model = YOLO('yolov8n.yaml') 

    # 3. Eğitimi başlat
    model.train(
    data='data.yaml', # config dosyası
    epochs=150,               
    imgsz=640,                
    batch=16,                 
    device=device,            
    workers=8,                
    project='runs_aug_stra_150_8n/train',
    name='traffic_sign',
    exist_ok=True,            
    save_period=10,          
    patience=25,             # early stopping
    cache=False              
)
    
if __name__ == '__main__':
    multiprocessing.freeze_support()
    train()
