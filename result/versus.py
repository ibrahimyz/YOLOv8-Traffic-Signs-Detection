import pandas as pd
import matplotlib.pyplot as plt

# 1. CSV yolları
runs = {
    'Baseline':   'runs/train/traffic_sign4/results.csv',
    'Augmented':  'runsAug/train/traffic_sign_aug/results.csv'
}

# 2. Verileri oku, F1 hesapla
data = {}
for label, path in runs.items():
    df = pd.read_csv(path)
    df['F1'] = 2 * df['metrics/precision(B)'] * df['metrics/recall(B)'] / (
                 df['metrics/precision(B)'] + df['metrics/recall(B)'])
    data[label] = df

# 3. mAP@0.5 Karşılaştırması
plt.figure(figsize=(10,4))
for label, df in data.items():
    plt.plot(df['epoch'], df['metrics/mAP50(B)'], label=label)
plt.title('mAP@0.5: Baseline vs Augmented')
plt.xlabel('Epoch'); plt.ylabel('mAP@0.5'); plt.legend()
plt.show()

# 4. F1 Karşılaştırması
plt.figure(figsize=(10,4))
for label, df in data.items():
    plt.plot(df['epoch'], df['F1'], label=label)
plt.title('F1 Score: Baseline vs Augmented')
plt.xlabel('Epoch'); plt.ylabel('F1 Score'); plt.legend()
plt.show()
