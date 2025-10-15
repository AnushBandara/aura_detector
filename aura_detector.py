import cv2
import numpy as np
import time
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
from deepface import DeepFace

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

overlay_vid = cv2.VideoCapture("green_vid.mp4")
green_lower = np.array([35, 100, 100])
green_upper = np.array([85, 255, 255])

pTime = 0  # For FPS calculation

colour_key = 0
c = [0, 0, 0]
mode_colour = [255, 0, 0]
mode = 0
dominant_emotion = "neutral"

segmentor = SelfiSegmentation()

while True:
    _, img = cap.read()

    ret, img_overlay = overlay_vid.read()
    if not ret:
        overlay_vid.set(cv2.CAP_PROP_POS_FRAMES, 5)
        continue
    img_overlay = cv2.cvtColor(cv2.resize(img_overlay, (640, 480)), cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(img_overlay, green_lower, green_upper)
    mask_invert = cv2.bitwise_not(mask)
    bubles = cv2.cvtColor(cv2.bitwise_and(img_overlay, img_overlay, mask=mask_invert), cv2.COLOR_HSV2BGR)

    lower_white = np.array([100, 100, 100])
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(bubles, lower_white, upper_white)
    color = np.array(mode_colour)
    bubles[mask > 0] = color

    overlay = img.copy()
    overlay[:] = mode_colour
    overlay = cv2.addWeighted(img, 0.9, overlay, 0.1, 0)

    vid = cv2.add(overlay, bubles)
    out = segmentor.removeBG(img, vid, cutThreshold=0.3)

    imgOut_mirrored = cv2.flip(out, 1)
    img_mirrored = cv2.flip(img, 1)
    cTime = time.time()
    fps = 1 / (cTime - pTime) if pTime != 0 else 0
    pTime = cTime
    cv2.putText(img_mirrored, f"Emotion : {dominant_emotion}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Aura Cam", imgOut_mirrored)
    cv2.imshow("Live Cam", img_mirrored)
    cv2.setWindowProperty("Live Cam", cv2.WND_PROP_TOPMOST, 1)

    key = cv2.waitKey(1)

    try:
        analysis_results = DeepFace.analyze(img, actions=['emotion'])
        first_face_results = analysis_results[0]
        dominant_emotion = first_face_results['dominant_emotion']
        print(f"Dominant emotion: {dominant_emotion}")
    except:
        print("problems in the paradise !")

    if dominant_emotion == 'happy':
        mode = 2
    elif dominant_emotion == 'angry':
        mode = 3
    elif dominant_emotion == 'surprise':
        mode = 4
    elif dominant_emotion == 'sad':
        mode = 1
    else:
        mode = 1

    if mode == 0: mode_colour = [0, 0, 0]
    if mode == 1: mode_colour = [255, 0, 0]  # Blue
    if mode == 2: mode_colour = [0, 255, 0]  # Green
    if mode == 3: mode_colour = [0, 0, 255]  # Red
    if mode == 4: mode_colour = [0, 255, 255]  # yellow

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
