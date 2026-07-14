import cv2
import time
import os

camera_number = 1

# 写真を保存するフォルダ
save_dir = "images"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("Camera could not be opened")
    raise SystemExit

photo_number = 1
last_save_time = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    cv2.imshow("USB Camera - press q to quit", frame)

    current_time = time.time()

    # 2秒ごとに写真を保存
    if current_time - last_save_time >= 2:
        filename = f"images/photo_{photo_number}.jpg"

        cv2.imwrite(filename, frame)

        print(f"Saved: {filename}")

        photo_number += 1
        last_save_time = current_time

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()