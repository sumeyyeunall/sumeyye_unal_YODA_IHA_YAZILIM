import cv2 #opencv görüntü işleme kütüphanesi
import time #sayac ve zaman ölçümü için 
import numpy as np #array işlemleri için 

#webcam ile başlatma
cap = cv2.VideoCapture(0) #sifir numarali cihaz pc kamerasını temsil ediyor

#OpenCV hazır yüz tanıma modeli OpenCV tarafindan default sağlanıyor
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#Hareket izi için,  yüzün merkez koordinatlarını saklamak için boş bir liste
pts = []
#zamanlayıcı değişkeni, yüz tespit edildiğinde sayacı başlatmak için başlangıç zamanı
start_time = None
#her frame için sonsuz döngü
while True:
    ret, frame = cap.read() #kameradan bir frame yakala
    #frame okunmadıysa break
    if not ret: 
        break
    #görüntüyü yatay olarak aynalama 
    frame = cv2.flip(frame, 1)
    #framei gritonlamaya çevirme
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #----yüz tespiti---
    #detectMultiScale metodu gri resimde yüzleri tespit eder
    # scaleFactor: her ölçekleme adımında boyutu büyütme yapar
    #minNeighbors: yüz olarak kabul edilecek minimum komşu sayısı
    #minSize: tespit edilecek en küçük yüz boyutu
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    if len(faces) > 0: #yüz tespit edildiyse
        #en geniş/büyük yüzü seç
        larg_face = max(faces, key=lambda rect: rect[2] * rect[3])
        #yüzün sol üst köşe koordinatları ve genişlik-yükseklik
        (x, y, w, h) = larg_face

        #face box ve center point 
        center = (int(x + w / 2), int(y + h / 2))
        #yüzün etrafına kırmızı bir dörtgen çizme
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #merkeze kırmzıı bir nokta koyma
        cv2.circle(frame, center, 5, (0, 0, 255), -1)
        cv2.putText(frame, f"Center: {center}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        #sol üst köşeye merkez koordinatlarını yazdırma


        #hareket izi:son 60 nokta
        pts.append(center) #merkez noktayi listeye ekliyoruz
        #eğer listedeki nokta sayısı 60ı geçtiyse en eski noktayı siliyoruz
        if len(pts) > 60:
            pts.pop(0)
        #noktaları birleştirerek hareketi çizme
        for i in range(1, len(pts)):
            if pts[i - 1] is None or pts[i] is None:
                continue
            #çizgi kalınlığını son noktalara göre değiştiriyoruz
            thickness = int(np.sqrt(64 / float(len(pts) - i + 1)) * 2)
            #kırmızı çizgi ile noktaları birleştiriyoruz
            cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)

        # saniye:salise sayacı sağ üst köşede 
        #sayaç başlamadıysa başlangıç zamanı alıyoruz 
        if start_time is None:
            start_time = time.time()
        #geçen süreyi hesaplama
        passed = time.time() - start_time
        seconds = int(passed)
        centiseconds = int((passed - seconds) * 100)
        #sayac metni
        timer_text = f"{seconds:02d}:{centiseconds:02d}"
        h_img, w_img, _ = frame.shape
        (text_w, text_h), _ = cv2.getTextSize(timer_text, cv2.FONT_HERSHEY_DUPLEX, 1, 2)
        #sağ üst box x koordinatı ve y koordinatı
        box_x1 = w_img - text_w - 20
        box_y1 = 10

        #içi boş kutu/ sayaç için çerçeve
        cv2.rectangle(frame, (box_x1 - 5, box_y1 - 5),
                      (w_img - 10, box_y1 + text_h + 10), (0, 0, 0), 2)

        #sayaç texti 
        cv2.putText(frame, timer_text, (box_x1, box_y1 + text_h),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

    else:
        #yüz tespit edilemedğinde sayacı sıfırlama ve pts listesini temizleme
        start_time = None
        pts = []

    #kameradan gelen framei göstr
    cv2.imshow("Face Tracking", frame)
    #esc tuşuna basıldığnda döngü sonlanır. 
    if cv2.waitKey(1) & 0xFF == 27:
        break
#kamera ve pencereleri kapatma 
cap.release()
cv2.destroyAllWindows()
