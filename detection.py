# from ultralytics import YOLO
# import math

# #Load YOLO11n model which I made
# model = YOLO("best.pt")

# #caluculate the center positon of each x and y
# def get_center(box):

#     #box = [x1,x2,y1,y2]
#     #Top-Left point (x1,y1)
#     #Bottom-Right point (x2,y2)

#     x1,y1, x2, y2 = box

#     center_x = (x1 + x2) / 2  #the average of x points
    
#     center_y = (y1 + y2) /2 #the average of y points

#     return center_x, center_y

# # get the distance of 2 points (using Euclid distance)
# def get_distance(point1,point2):

#     x1,y1 = point1
#     x2,y2 = point2

#     distance = math.sqrt((x1 - x2) **2 + (y1-y2) **2)

#     return distance

# def detection(frame):

#     #Run YOLO detection on the camera frame
#     reuslts = model(frame, verbose=False)

#     #detection objects lists
#     phones = []
#     hands = []
#     persons = []
#     faces = []

#     #check all detection results

#     for result in results:
#         for box in result.boxes:

#             #

#temporarily code
from ultralytics import YOLO
import math


# best.pt model is loaded here
# Change the path if best.pt is in another folder
model = YOLO("best.pt")


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
    #It is used to check whether hand and phone are close.
    x1, y1 = point1
    x2, y2 = point2

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

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
    phones = []
    hands = []
    persons = []
    faces = []

    # Check all detection results
    for result in results:
        for box in result.boxes:

            # class id
            class_id = int(box.cls[0])

            # class name, for example: phone, hand, person
            class_name = model.names[class_id]

            # confidence score
            confidence = float(box.conf[0])

            # Ignore low confidence detection
            if confidence < 0.5:
                continue

            # Get box position
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            # Save detected objects by class name
            if class_name in ["phone", "smartphone", "cell phone"]:
                phones.append([x1, y1, x2, y2])

            elif class_name in ["hand", "hands"]:
                hands.append([x1, y1, x2, y2])

            elif class_name in ["person", "user"]:
                persons.append([x1, y1, x2, y2])

            elif class_name in ["face"]:
                faces.append([x1, y1, x2, y2])

    # Sitting detection
    # If person or face is detected, the user is sitting
    if len(persons) > 0 or len(faces) > 0:
        is_sitting = True
    else:
        is_sitting = False

    # Smartphone usage detection
    is_using_phone = False

    for phone in phones:
        phone_center = get_center(phone)

        for hand in hands:
            hand_center = get_center(hand)

            # Calculate distance between phone and hand
            hand_phone_distance = get_distance(phone_center, hand_center)

            # If hand and phone are close, judge as smartphone usage
            if hand_phone_distance < 150:
                is_using_phone = True
                break

        if is_using_phone:
            break

    return is_sitting, is_using_phone