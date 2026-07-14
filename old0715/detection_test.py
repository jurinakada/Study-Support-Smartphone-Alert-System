from ultralytics import YOLO
import cv2
import math
import time


# Load the custom YOLO model
model = YOLO("best.pt")


def get_center(box):
    """
    Calculate the center point of a bounding box.

    box = [x1, y1, x2, y2]
    """

    x1, y1, x2, y2 = box

    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2

    return center_x, center_y


def get_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.
    """

    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt(
        (x1 - x2) ** 2
        + (y1 - y2) ** 2
    )

    return distance


def detection(frame):
    """
    Detect whether:
    1. The user is sitting
    2. The user is holding or using a smartphone

    Returns:
        is_sitting: bool
        is_using_phone: bool
    """

    # Run YOLO detection
    results = model(frame, verbose=False)

    phones = []
    hands = []
    persons = []
    faces = []

    for result in results:
        for box in result.boxes:

            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            confidence = float(box.conf[0])

            # Ignore low-confidence detections
            if confidence < 0.5:
                continue

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            detected_box = [x1, y1, x2, y2]

            if class_name in ["phone", "smartphone", "cell phone"]:
                phones.append(detected_box)

            elif class_name in ["hand", "hands"]:
                hands.append(detected_box)

            elif class_name in ["person", "user"]:
                persons.append(detected_box)

            elif class_name == "face":
                faces.append(detected_box)

    # Sitting detection
    is_sitting = len(persons) > 0 or len(faces) > 0

    # Smartphone usage detection
    is_using_phone = False

    for phone in phones:
        phone_center = get_center(phone)

        for hand in hands:
            hand_center = get_center(hand)

            hand_phone_distance = get_distance(
                phone_center,
                hand_center
            )

            if hand_phone_distance < 150:
                is_using_phone = True
                break

        if is_using_phone:
            break

    return is_sitting, is_using_phone


def main():
    """
    Standalone test using a USB camera.
    Press q to stop.
    """

    camera_number = 0

    # Open USB camera
    camera = cv2.VideoCapture(camera_number)

    if not camera.isOpened():
        print("Error: Camera could not be opened.")
        print("Try changing camera_number from 0 to 1.")
        return

    # Set camera resolution
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    print("Camera test started.")
    print("Press q to stop.")

    previous_time = time.time()

    try:
        while True:

            success, frame = camera.read()

            if not success:
                print("Error: Failed to capture frame.")
                break

            # Run the detection function
            is_sitting, is_using_phone = detection(frame)

            # Print results in the terminal
            print(
                f"\rSitting: {is_sitting} | "
                f"Using phone: {is_using_phone}",
                end=""
            )

            # Calculate FPS
            current_time = time.time()
            elapsed_time = current_time - previous_time

            if elapsed_time > 0:
                fps = 1 / elapsed_time
            else:
                fps = 0

            previous_time = current_time

            # Change boolean values into readable text
            if is_sitting:
                sitting_text = "SITTING: YES"
            else:
                sitting_text = "SITTING: NO"

            if is_using_phone:
                phone_text = "PHONE USE: YES"
            else:
                phone_text = "PHONE USE: NO"

            # Display the result on the camera frame
            cv2.putText(
                frame,
                sitting_text,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0) if is_sitting else (0, 0, 255),
                2
            )

            cv2.putText(
                frame,
                phone_text,
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255) if is_using_phone else (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"FPS: {fps:.1f}",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

            # Show camera image
            cv2.imshow("YOLO Detection Test", frame)

            # Press q to stop
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                print("\nTest stopped by user.")
                break

    except KeyboardInterrupt:
        print("\nTest stopped by KeyboardInterrupt.")

    finally:
        camera.release()
        cv2.destroyAllWindows()
        print("Camera closed.")


if __name__ == "__main__":
    main()