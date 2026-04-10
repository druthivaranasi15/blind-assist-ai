# Blind Assist AI

##  Overview
Blind Assist AI is a basic real-time computer vision system that detects objects using YOLOv8 and provides voice feedback for scene awareness.

This project demonstrates how object detection models can be integrated with text-to-speech to create an assistive system.

---

##  Features
- Real-time object detection using YOLOv8
- Webcam-based input
- Converts detected objects into speech
- Non-blocking speech using threading
- Simple scene awareness output

---

##  Tech Stack
- Python
- OpenCV
- YOLOv8 (Ultralytics)
- pyttsx3 (Text-to-Speech)
- Threading

---

##  How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/blind-assist-ai.git
cd blind-assist-ai
```
### 2.Install dependencies
pip install -r requirements.txt
### 3. Run the project
python main.py

## How It Works
1.Captures live video using webcam
2.Uses YOLOv8 model to detect objects
3.Extracts object labels
4.Converts labels into a sentence
5.Uses text-to-speech to speak the result


## Future Improvements
1.Add object direction detection (left/right)
2.Improve detection stability using tracking
3.Optimize for mobile or edge devices
4.Add custom-trained model for better accuracy







dt-ai
