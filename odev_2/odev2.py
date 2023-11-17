import cv2
import numpy as np

goruntu = cv2.VideoCapture(0)

while True:
    ret, frame = goruntu.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    koyu_kirmizi = np.array([0, 100, 100])
    acik_kirmizi= np.array([25, 255, 255])

    maske = cv2.inRange(hsv, koyu_kirmizi, acik_kirmizi)
    cikti = cv2.bitwise_and(frame, frame, mask=maske)

    cv2.imshow('Orijinal Goruntu', frame)
    cv2.imshow('Sadece Kirmizi', cikti)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
goruntu.release()
cv2.destroyAllWindows()

