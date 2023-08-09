import cv2
import time
from yolov8 import YOLOv8
from components.config import *

# Initialize the webcam
cap = cv2.VideoCapture("/dev/video0")

# Initialize YOLOv8 object detector
model_path = "./models/yolov8s.onnx"
yolov8_detector = YOLOv8(model_path, conf_thres=0.5, iou_thres=0.5)

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)

if STATUS_LATENCY == 1:
    print("pengukuran latensi aktif, tekan q untuk melihat hasil")
    latency_values = []  # To store latency values
    fps_values = []
else:
    print("pengukuran latensi tidak aktif,lakukan aktivasi pada file config")

while cap.isOpened():
    if STATUS_LATENCY == 1:
        start_time = time.time()

    # Read frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Update object localizer
    boxes, scores, class_ids = yolov8_detector(frame)

    combined_img = yolov8_detector.draw_detections(frame)
    if STATUS_LATENCY == 1:
        end_time = time.time()
        latency = end_time - start_time
        fps = 1/latency 
        latency_values.append(latency)
        fps_values.append(fps)

    cv2.imshow("Detected Objects", combined_img)
    # Press key q to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

if STATUS_LATENCY == 1:
    average_latency = sum(latency_values) / len(latency_values)
    average_FPS = sum(fps_values)/len(fps_values)
    print(f"Average Latency: {average_latency:.4f} seconds")
    print(f"Average FPS: {average_FPS:.4f}")


# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
