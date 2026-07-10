import cv2


class Camera:
    def __init__(self, camera_number=0):
        self.cap = cv2.VideoCapture(camera_number)

        if self.cap.isOpened() == False:
            raise RuntimeError("Failed to open the USB camera")

    def capture_frame(self):
        # Capture one frame from the USB camera
        ret, frame = self.cap.read()

        if ret == False:
            print("Failed to capture an image")
            return None

        return frame

    def close(self):
        # Release the USB camera
        self.cap.release()
        print("Camera was closed")


#temporarily codes
# from detection import detection
# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     if not ret:
#         break

#     is_sitting, is_using_phone = detection(frame)

#     print("Sitting:", is_sitting)
#     print("Using phone:", is_using_phone)

#     if is_sitting and is_using_phone:
#         print("Warning: Smartphone use detected")

# cap.release()