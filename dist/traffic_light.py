import cv2
import numpy as np

def detect_traffic_light_status(frame, roi):
    x1, y1, x2, y2 = roi
    cropped = frame[y1:y2, x1:x2]
    hsv = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)

    # tons de vermelho (0-10 e 160-180 em H)
    mask_red1 = cv2.inRange(hsv, (0, 100, 100), (10, 255, 255))
    mask_red2 = cv2.inRange(hsv, (160, 100, 100), (180, 255, 255))
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # tons de verde mais abrangente
    mask_green = cv2.inRange(hsv, (35, 60, 60), (85, 255, 255))

    red_pixels = cv2.countNonZero(mask_red)
    green_pixels = cv2.countNonZero(mask_green)

    print(f"[DEBUG] Vermelho: {red_pixels} pixels | Verde: {green_pixels} pixels")

    if red_pixels > 100:
        return "red"
    elif green_pixels > 100:
        return "green"
    return "unknown"
