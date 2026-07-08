import cv2
import time
import os

save_dir = "images"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)

try:
    while True:

        ret, frame = cap.read()

        if ret:
            filename = f"{save_dir}/image_{i:03d}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved: {filename}")

        time.sleep(2)


except KeyboardInterrupt:
    cap.release()