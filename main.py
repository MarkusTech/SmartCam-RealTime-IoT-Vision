import cv2
import base64
from io import BytesIO
from PIL import Image
import numpy as np
import os
from dotenv import load_dotenv
from utils.huggingface_api import analyze_image
from iot.device_control import handle_command

load_dotenv()

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Press 'q' to quit, 's' to analyze frame, '1'/'2' to simulate IoT commands.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting...")
        break

    cv2.imshow('SmartCam AI', frame)

    key = cv2.waitKey(1) & 0xFF

    # Quit
    if key == ord('q'):
        break

    # Analyze frame
    elif key == ord('s'):
        # Convert frame to bytes
        _, buffer = cv2.imencode('.jpg', frame)
        image_bytes = buffer.tobytes()

        result = analyze_image(image_bytes)
        print("Hugging Face Result:", result)

    # IoT commands simulation
    elif key == ord('1'):
        print(handle_command("turn-on-light"))
    elif key == ord('2'):
        print(handle_command("turn-off-light"))

cap.release()
cv2.destroyAllWindows()
