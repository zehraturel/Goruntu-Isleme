import cv2
import numpy as np

# görsel yükle
foto = cv2.imread('C:\\Users\\zehra\\Documents\\GitHub\\Goruntu-Isleme\\odev_3\\ornek.png', cv2.IMREAD_COLOR)
foto_rgb = cv2.cvtColor(foto, cv2.COLOR_BGR2RGB)  # BGR'den RGB'ye dönüşüm

# Otsu thresholding uygula
gray = cv2.cvtColor(foto, cv2.COLOR_RGB2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Gürültüyü azaltmak için morfolojik açılım uygula
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=50)

# Konturları bul
kontur, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Pirinç tanesi sayısı
pirinc_adeti = len(kontur)
print(f"Pirinç tanesi sayisi: {pirinc_adeti}")

# Konturları orijinal görüntüde görselleştir
result = foto_rgb.copy()
cv2.drawContours(result, kontur, -1, (0, 255, 0), 2)

# Görüntüleri göstermeden önce pencereye sığmaları için tekrar boyutlandırma işlemi uygula.
result = cv2.resize(result, (500,500))
small_image = cv2.resize(thresh, (500,500))  # Yeni genişlik ve yükseklik değerlerini belirleyin

cv2.imshow('Thresholding Uygulanmiş Resim', small_image)
cv2.imshow('Konturlar', result)

cv2.waitKey(0)
cv2.destroyAllWindows()