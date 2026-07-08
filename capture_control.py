import cv2
from detection import detection

#temporarily codes

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    is_sitting, is_using_phone = detection(frame)

    print("Sitting:", is_sitting)
    print("Using phone:", is_using_phone)

    if is_sitting and is_using_phone:
        print("Warning: Smartphone use detected")

cap.release()