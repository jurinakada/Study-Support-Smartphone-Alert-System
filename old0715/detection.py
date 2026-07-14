from ultralytics import YOLO
import math
import os


# best.pt model is loaded here
# best.pt is loaded from the same folder as detection.py
model_path = os.path.join(
    os.path.dirname(__file__),
    "best.pt"
)

model = YOLO(model_path)


def get_center(box):
    #This function calculates the center point of a detected box.

    #box = [x1, y1, x2, y2]
    #x1, y1 = left top position
    #x2, y2 = right bottom position
    x1, y1, x2, y2 = box

    center_x = (x1 + x2) / 2
    center_y = (y1 + y2) / 2

    return center_x, center_y


def get_distance(point1, point2):
    #This function calculates the distance between two points.
    #It is used to check whether hand and smartphone are close.
    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt(
        (x1 - x2) ** 2
        + (y1 - y2) ** 2
    )

    return distance


def detection(frame):
    #This function detects:
    # 1. whether the user is sitting
    # 2. whether the user is using / holding a smartphone

    # return:
    #     is_sitting
    #     is_using_phone

    # Run YOLO detection on the camera frame
    results = model(frame, verbose=False)

    # Lists for detected objects
    smartphones = []
    hands = []
    persons = []

    # Check all detection results
    for result in results:
        for box in result.boxes:

            # class id
            class_id = int(box.cls[0])

            # class name: person, smartphone, or hand
            class_name = str(
                model.names[class_id]
            ).lower().strip()

            # confidence score
            confidence = float(box.conf[0])

            # Ignore low confidence detection
            if confidence < 0.5:
                continue

            # Get box position
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            # Save detected objects by class name
            if class_name == "smartphone":
                smartphones.append(
                    [x1, y1, x2, y2]
                )

            elif class_name == "hand":
                hands.append(
                    [x1, y1, x2, y2]
                )

            elif class_name == "person":
                persons.append(
                    [x1, y1, x2, y2]
                )

    # Sitting detection
    # If person is detected, the user is sitting
    if len(persons) > 0:
        is_sitting = True

    else:
        is_sitting = False

    # Smartphone usage detection
    is_using_phone = False

    for smartphone in smartphones:
        smartphone_center = get_center(
            smartphone
        )

        for hand in hands:
            hand_center = get_center(hand)

            # Calculate distance between smartphone and hand
            hand_phone_distance = get_distance(
                smartphone_center,
                hand_center
            )

            # If hand and smartphone are close,
            # judge as smartphone usage
            if hand_phone_distance < 150:
                is_using_phone = True
                break

        if is_using_phone == True:
            break

    return is_sitting, is_using_phone