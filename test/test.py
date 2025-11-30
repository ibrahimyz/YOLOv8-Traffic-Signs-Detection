from ultralytics import YOLO

def main():
    best_model_path = "bestModel.pt"  # Path to your best model weights
    
    # 1. Load your best weights
    model = YOLO(best_model_path)
    
    # 2. Run validation on the test split defined in data.yaml
    results = model.val(data='data.yaml', split='test')

if __name__ == '__main__':
    import multiprocessing
    multiprocessing.freeze_support()  # optional unless you're creating an executable
    main()