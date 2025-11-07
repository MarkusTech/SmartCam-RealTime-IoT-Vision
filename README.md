# SmartCam-RealTime-IoT-Vision

A Python project that combines **real-time webcam AI analysis** with **simulated IoT device control**.

### Features

- Live camera feed using OpenCV
- Send captured frames to Hugging Face for object recognition
- Simulated IoT device commands (turn on/off lights)
- Easy to extend for real IoT hardware (Raspberry Pi, sensors, etc.)

### Requirements

- Python 3.9+
- Hugging Face API Key

### Installation

```bash
git clone https://github.com/MarkusTech/SmartCam-RealTime-IoT-Vision.git
cd SmartCam-RealTime-IoT-Vision
pip install -r requirements.txt
cp .env.example .env
# Add your Hugging Face API key to .env
```
