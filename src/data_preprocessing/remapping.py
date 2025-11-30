# remapping.py
# Bu betik, etiket dosyalarındaki sınıf kimliklerini yeniden eşlemek için kullanılır.

remap_whole_to_last = {
    0: 0,    
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    13: 13,
    14: 14,
    15: 15,
    17: 16,
    18: 17,
    20: 18,
    21: 19,
    22: 20,
    23: 21,
    24: 22,
    25: 23,
    26: 24,
    27: 26,
    28: 27,
    29: 28,
    30: 25
}
 
WHOLE_DATA_PATH = "lastDataset"  # Bu, son dataset klasörünün adı
 
import os
import shutil
 
 
# Path’ler
 
base_path = os.path.join(r"project\\path", WHOLE_DATA_PATH) # Daha güvenli yol birleştirme
 
print(f"Base path: {base_path}")
labels_dir = os.path.join(base_path, "labels")
images_dir = os.path.join(base_path, "images")
print(f"Labels directory: {labels_dir}") # Add this
print(f"Images directory: {images_dir}") # Add this
 
# Çıktı klasörleri
output_path = r"output\\remapped_dataset"
 
os.makedirs(output_path, exist_ok=True)
 
output_labels  = os.path.join(output_path, "labels")
output_images  = os.path.join(output_path, "images")
 
os.makedirs(output_labels, exist_ok=True)
os.makedirs(output_images, exist_ok=True)
 
remap_name = remap_whole_to_last
 
counter = 1
 
for fname in sorted(os.listdir(labels_dir)):
    if not fname.endswith(".txt"):
        continue
 
    in_txt = os.path.join(labels_dir, fname)
    stem = fname[:-4]  # strip “.txt”
 
    # 1) Read, filter & remap
    with open(in_txt, "r") as fr:
        orig_lines = [l.strip() for l in fr if l.strip()]
 
    filtered = []
    for line in orig_lines:
        parts = line.split()
        cid = int(parts[0])
        if cid in remap_name:
            parts[0] = str(remap_name[cid])
            filtered.append(" ".join(parts))
        # else: drop
 
    # 2) If no labels remain, remove txt+image and skip
    if not filtered:
        print(f"Removing '{fname}' (no mapped labels) and its image.")
        os.remove(in_txt)
        for ext in (".jpg", ".png"):
            img_path = os.path.join(images_dir, stem + ext)
            if os.path.exists(img_path):
                os.remove(img_path)
                print(f"Deleted image: {img_path}")
                break
        continue
 
    # 3) Otherwise write out filtered labels
    out_txt = os.path.join(output_labels, stem  + ".txt") #stem f"_{counter}"
    with open(out_txt, "w") as fw:
        fw.write("\n".join(filtered) + "\n")
 
    # 4) Copy corresponding image
    for ext in (".jpg", ".png"):
        src = os.path.join(images_dir, stem + ext)
        if os.path.exists(src):
            dst = os.path.join(output_images, stem  + ext)
            shutil.copy(src, dst)
            print(f"→ {fname}  ➔ {stem}.txt  and  {stem}{ext}")
            break
 
    counter += 1
 
print(f"\nToplam {counter-1} label eşitlendi ve dosyalar yeniden adlandırıldı.")