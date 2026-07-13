import cv2
import time
import os
import glob

save_dir = "images"
os.makedirs(save_dir, exist_ok=True)

camera_number = 1
cap = cv2.VideoCapture(camera_number, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("Error: Camera is not open")
    raise SystemExit

# 既存画像の続きの番号から保存
existing_images = glob.glob(os.path.join(save_dir, "image_*.jpg"))

if existing_images:
    numbers = []

    for image_path in existing_images:
        filename = os.path.basename(image_path)
        number_text = filename.replace("image_", "").replace(".jpg", "")

        if number_text.isdigit():
            numbers.append(int(number_text))

    image_number = max(numbers) if numbers else 0
else:
    image_number = 0

last_save_time = time.time()

save_interval = 2
max_images = 100
saved_count = 0

print(f"Start from image number: {image_number + 1}")

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break

        cv2.imshow("USB Camera - press q to quit", frame)

        current_time = time.time()

        if current_time - last_save_time >= save_interval:
            image_number += 1
            saved_count += 1

            filename = os.path.join(
                save_dir,
                f"image_{image_number:03d}.jpg"
            )

            if cv2.imwrite(filename, frame):
                print(f"Saved: {filename}")
            else:
                print(f"Failed to save: {filename}")

            last_save_time = current_time

            if saved_count >= max_images:
                print(f"Collected {max_images} new images")
                break

        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Stopped Camera")
            break

except KeyboardInterrupt:
    print("Stopped Camera by pressing Ctrl + C")

finally:
    cap.release()
    cv2.destroyAllWindows()