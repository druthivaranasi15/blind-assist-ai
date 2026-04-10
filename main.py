import cv2 
from ultralytics import YOLO

import pyttsx3
engine=pyttsx3.init()

import time
import threading

model=YOLO("yolov8s.pt")

cap=cv2.VideoCapture(0)

prev_objects=set()
last_spoken_time=0
cooldown =4

def speak(text):
     engine.say(text)
     engine.runAndWait()

while True:
        ret,frame=cap.read()

        if not ret:
                print("Failed to grab frame")
                break

        results = model(frame, conf=0.25)

        detected_objects=[]

        for box in results[0].boxes:
               cls = int(box.cls)
               label = model.names[cls]
               detected_objects.append(label)

        print(detected_objects)

        current_time=time.time()
        current_objects= set(detected_objects)

        if current_objects:
               if current_objects!=prev_objects or (current_time - last_spoken_time > cooldown):
               
                sentence = "I see " + ", ".join(current_objects)
                print(sentence)

                threading.Thread(target=speak, args=(sentence,)).start()

                last_spoken_time=current_time

        prev_objects = current_objects

        annotated_frame = results[0].plot()

        cv2.imshow("Blind Assist AI", annotated_frame)

        key=cv2.waitKey(1) & 0xFF
        if key==27:
              break

cap.release()
cv2.destroyAllWindows()