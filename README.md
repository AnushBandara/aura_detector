# Aura Detector – Where Emotions Meet Code 🎥💭

Aura Detector is a real-time **emotion-based background visualizer** built with **Python**, **OpenCV**, **DeepFace**, and **cvzone**.

It detects your facial **emotion through the webcam** and dynamically changes the background aura using colors and bubble-like animations — turning your mood into motion.  
Inspired by the idea that every person emits an “aura” — an invisible energy or vibe that reflects their emotional state — this project brings that concept to life through computer vision.

---

## 🎬 Demo
👉 *[https://youtu.be/LH9PGXwQnDs]*  

---

## 🧠 Features
- 🎭 Real-time **emotion detection** with DeepFace  
- ✨ **Aura visualization** based on emotion  
- 🪄 **Background segmentation** using cvzone SelfieSegmentation  
- ⚡ Optimized live video rendering with OpenCV  
- 🧩 Easy to modify and extend with new effects or colors  

---

## 🌈 Emotion-to-Color Mapping
| Emotion   | Aura Color | Description |
|------------|-------------|--------------|
| Happy 😊 | Green 💚 | Calm and energetic |
| Sad 😢 | Blue 💙 | Cool and peaceful |
| Angry 😡 | Red ❤️ | Intense and fiery |
| Surprise 😮 | Yellow 💛 | Bright and lively |
| Neutral 😐 | Blue 💙 | Default calm tone |

---

## 🛠️ Tech Stack
- **Python 3.x**
- **OpenCV** – for video capture and image processing  
- **DeepFace** – for facial emotion recognition  
- **cvzone** – for real-time background segmentation  
- **NumPy** – for efficient matrix operations  

---

## ⚙️ Installation

```bash
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/aura-detector.git
cd aura-detector

# 2️⃣ Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # on macOS/Linux
venv\Scripts\activate      # on Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the project
python aura_detector.py
