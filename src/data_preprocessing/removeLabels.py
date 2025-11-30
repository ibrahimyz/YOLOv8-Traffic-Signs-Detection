import os
 
def remove_labels_from_files(
    base_names: list[str],
    labels_dir: str,
    images_dir: str,
    remove_cids: set[int]
):
    """
    For each stem in base_names, remove any label lines in labels_dir/<stem>.txt
    whose class ID is in remove_cids. If a file becomes empty, delete it and
    its image (.jpg or .png) in images_dir.
    """
    for stem in base_names:
        txt_path = os.path.join(labels_dir, stem)
        if not os.path.exists(txt_path):
            print(f"[SKIP] Label file not found: {txt_path}")
            continue
 
        # Read & filter
        with open(txt_path, "r") as f:
            lines = [l.strip() for l in f if l.strip()]
        kept = []
        for line in lines:
            parts = line.split()
            cid = int(parts[0])
            if cid not in remove_cids:
                kept.append(line)
 
        if kept:
            # Write back only the kept lines
            with open(txt_path, "w") as f:
                f.write("\n".join(kept) + "\n")
            print(f"[UPDATED] {stem} — removed classes {remove_cids & {int(l.split()[0]) for l in lines}}")
        else:
            # No labels left: delete txt + image
            os.remove(txt_path)
            print(f"[DELETED] {stem} (no labels left)")
            for ext in (".jpg", ".png"):
                img_path = os.path.join(images_dir, stem.replace(".txt","") + ext)
                if os.path.exists(img_path):
                    os.remove(img_path)
                    print(f"[DELETED] Image: {img_path}")
                    break
 
# --- Usage example ---
labels_dir = "path_to_labels_dir"
images_dir = "path_to_images_dir"
 
to_fix = os.listdir(labels_dir)
cids_to_remove = {26, 27, 28}
 
remove_labels_from_files(to_fix, labels_dir, images_dir, cids_to_remove)