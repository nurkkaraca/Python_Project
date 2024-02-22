import cv2

resim = cv2.imread ("everest.jpg")
cv2.imshow("everest",resim)
cv2.waitKey(0)
cv2.imshow("everest",resim)
yukseklik = resim.shape[0]
genislik = resim.shape[1]
print('Resim Yüksekliği (px)      :', yukseklik)
print('Resim Genişliği  (px)     :', genislik)
cv2.waitKey(0)
cv2.destroyAllWindows()