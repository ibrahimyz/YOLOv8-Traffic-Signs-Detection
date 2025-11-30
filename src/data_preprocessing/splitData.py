import os
import random
import shutil

# Ayarlar # Kendinize göre düzenleyin!
SRC_IMG = "data/images"
SRC_LBL = "data/labels"
DEST_IMG = "data_split/images"
DEST_LBL = "data_split/labels"

RATIO = {
    "train": 0.7,
    "val":   0.15,
    "test":  0.15
}

# Oluşturulacak klasörler
for split in RATIO:
    os.makedirs(os.path.join(DEST_IMG, split), exist_ok=True)
    os.makedirs(os.path.join(DEST_LBL, split), exist_ok=True)

# Tüm görüntü dosyalarını listele
all_imgs = [f for f in os.listdir(SRC_IMG) if f.endswith((".jpg", ".png"))]
random.seed(42)
random.shuffle(all_imgs)

n = len(all_imgs)
n_train = int(RATIO["train"] * n)
n_val   = int(RATIO["val"]   * n)
# geriye kalan test
n_test  = n - n_train - n_val

splits = {
    "train": all_imgs[:n_train],
    "val":   all_imgs[n_train:n_train+n_val],
    "test":  all_imgs[n_train+n_val:]
}

# Dosyaları kopyala
for split, files in splits.items():
    print(f"{split} setinde {len(files)} dosya var.")
    for img_name in files:
        # Görsel
        src_img_path = os.path.join(SRC_IMG, img_name)
        dst_img_path = os.path.join(DEST_IMG, split, img_name)
        shutil.copy(src_img_path, dst_img_path)

        # Aynı ada sahip label
        lbl_name = os.path.splitext(img_name)[0] + ".txt"
        src_lbl_path = os.path.join(SRC_LBL, lbl_name)
        dst_lbl_path = os.path.join(DEST_LBL, split, lbl_name)
        if os.path.exists(src_lbl_path):
            shutil.copy(src_lbl_path, dst_lbl_path)
        else:
            # Label dosyası yoksa istersen uyarı ver
            print(f"UYARI: Label bulunamadı: {lbl_name}")
