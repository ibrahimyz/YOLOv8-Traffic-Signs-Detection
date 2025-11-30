from ultralytics import YOLO
import cv2

# Eğitilmiş modelin yüklenmesi
model = YOLO("bestModel.pt")  # Modeli seç

# Kamerayı başlat (0 = varsayılan web kamera)
cap = cv2.VideoCapture(0)

# Kamera açıksa döngü başlasın
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO modeli ile tahmin
    results = model(frame, stream=True)

    # Sonuçları çiz
    for r in results:
        annotated_frame = r.plot()  # tespitleri çizilmiş hali

    # Görseli göster
    cv2.imshow("YOLO Real Time Detection", annotated_frame)

    # 'q' tuşuna basınca çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Temizlik
cap.release()
cv2.destroyAllWindows()
