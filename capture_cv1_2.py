import cv2
import time
import os

save_dir = "images"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
#720p
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)

if not cap.isOpened():
    print("Error: Camera is not open")
    exit()

i= 0;
last_save_time = time.time()

try:
    while True:
        i = i + 1
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to capture frame")
        
        cv2.imshow("USB Camera quit with q", frame)
        
        current_time = time.time()
        
        if current_time - last_save_time >= 2:
            i += 1
            filename = f"{save_dir}/image_{i:03d}.jpg"
            cv2.imwrite(filename, frame)
            print(f"Saved: {filename}")
        lst_save_time = current_time

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Stopped Camera")
            break


except KeyboardInterrupt:
    print("Stopped Camera by pressing Ctrl + C")

finally:
    cap.release()
    cv2.destroyAllWindows()
