import cv2
from ultralytics import YOLO
 
# Eğittiğiniz modelin yüklenmesi
model = YOLO('last_model.pt')
 
# Telefon IP webcam'den görüntü akışı
stream_url = ''  # bu adresi IP Webcam uygulaması verir
 
while True:
    frame_resp = cv2.VideoCapture(stream_url)
    ret, frame = frame_resp.read()
    if not ret:
        continue
 
    results = model.predict(source=frame, conf=0.4)
 
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = f"{model.names[cls]} {conf:.2f}"
 
            # Kutu ve tahmin yazısı
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, label, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
 
    # Ekrana anlık görüntüyü yaz
    cv2.imshow("Phone Cam Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
 
cv2.destroyAllWindows()
 