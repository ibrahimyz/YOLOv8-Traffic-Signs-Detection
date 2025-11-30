import pandas as pd
import matplotlib.pyplot as plt

# 1. Dosyanın tam yolunu belirtin
csv_path = 'runs/train/traffic_sign4/results.csv'

# 2. CSV'i oku
df = pd.read_csv(csv_path)

# 3. F1 Score'u hesapla
df['F1'] = 2 * df['metrics/precision(B)'] * df['metrics/recall(B)'] \
             / (df['metrics/precision(B)'] + df['metrics/recall(B)'])

# 4. Tabloyu göz atmak istersen:
print(df[['epoch',
          'metrics/precision(B)',
          'metrics/recall(B)',
          'metrics/mAP50(B)',
          'metrics/mAP50-95(B)',
          'F1']].to_string(index=False))

# 5. Grafikleri çiz

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.plot(df['epoch'], df['metrics/mAP50(B)'], marker='o')
plt.title('mAP@0.5 vs Epoch')
plt.xlabel('Epoch'); plt.ylabel('mAP@0.5')

plt.subplot(1,3,2)
plt.plot(df['epoch'], df['metrics/precision(B)'], label='Precision')
plt.plot(df['epoch'], df['metrics/recall(B)'],  label='Recall')
plt.title('Precision & Recall vs Epoch')
plt.xlabel('Epoch'); plt.legend()

plt.subplot(1,3,3)
plt.plot(df['epoch'], df['F1'], color='orange', marker='s')
plt.title('F1 Score vs Epoch')
plt.xlabel('Epoch'); plt.ylabel('F1 Score')

plt.tight_layout()
plt.show()
