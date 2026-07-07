import cv2


def enhance_image(image):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    image = clahe.apply(image)
    image = cv2.GaussianBlur(image, (5, 5), 0)
    return image


cap = cv2.VideoCapture(0)

arac_sollama_levhasi = cv2.CascadeClassifier('arac_sollamak_yasak_levhasi.xml')
park_levhasi = cv2.CascadeClassifier('park_levhasi.xml')
demir_yolu_levhasi = cv2.CascadeClassifier('demir_yolu_levhasi.xml')
yaya_gecidi_levhasi = cv2.CascadeClassifier('yaya_gecidi_levhasi.xml')

arac_sollama_factor = 1.3
park_factor = 1.3
demir_yolu_factor = 1.4
yaya_gecidi_factor = 1.3

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = enhance_image(gray)

    arac_sollamak_yasak = arac_sollama_levhasi.detectMultiScale(gray, scaleFactor=arac_sollama_factor, minNeighbors=5,
                                                                minSize=(30, 30))

    for (x, y, w, h) in arac_sollamak_yasak:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Arac Sollama", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    park = park_levhasi.detectMultiScale(gray, scaleFactor=park_factor, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in park:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, "Park", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    demir_yolu = demir_yolu_levhasi.detectMultiScale(gray, scaleFactor=demir_yolu_factor, minNeighbors=5,
                                                     minSize=(30, 30))

    for (x, y, w, h) in demir_yolu:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(frame, "Demir Yolu", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    yaya_gecidi = yaya_gecidi_levhasi.detectMultiScale(gray, scaleFactor=yaya_gecidi_factor, minNeighbors=5,
                                                       minSize=(30, 30))

    for (x, y, w, h) in yaya_gecidi:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        cv2.putText(frame, "Yaya Gecidi", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 0), 2)

    resized_frame = cv2.resize(frame, (250, 100))

    cv2.imshow('Kamera', resized_frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
