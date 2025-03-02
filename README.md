✋ Hand Gesture Recognition using Mediapipe 🤖

🌟 Overview

This project implements a Hand Gesture Recognition system using OpenCV and Mediapipe. It can accurately identify and classify different hand gestures from image or video data, enabling intuitive human-computer interaction and gesture-based control systems. 🎥💡

🚀 Features

🎯 Real-time hand gesture detection

✌️ Multiple gestures supported: 👍, 👌, ✊, 🤘, 🤙, ✌️, etc.

🖐 Uses Mediapipe's hand tracking model for fast and efficient gesture recognition

📷 Works with live webcam feed

🔥 Simple and lightweight implementation

🖐 Hand Landmark Reference

Mediapipe detects 21 landmarks on the hand, as shown in the image below:



⚙️ Installation

To run this project, you need to install the required dependencies. Run the following command:

pip install opencv-python mediapipe numpy

▶️ Usage

To start the hand gesture recognition system, simply run the Python script:

python hand_gesture_recognition.py

The system will open your webcam and begin detecting hand gestures in real time. 🎥📌

🧠 Hand Gesture Detection Logic

This project uses the angle between finger joints to determine if a finger is open or closed. Based on this information, gestures are classified into different categories:

Gesture Name

### Hand Gesture Recognition - Finger States

| Gesture    | Finger State (1 = Open, 0 = Closed) | Description |
|------------|----------------------------------|-------------|
| 👍 **Thumbs Up** | `[1, 0, 0, 0, 0]` | Only the thumb is open |
| 👌 **OK Sign** | `[0, 1, 1, 1, 1]` + Thumb touching Index | Index, middle, ring, pinky open, thumb touching index |
| 🤘 **Rock** | `[0, 1, 0, 0, 1]` | Index and pinky open |
| 🤙 **Call Me** | `[1, 0, 0, 0, 1]` | Thumb and pinky open |
| ✌️ **Victory** | `[0, 1, 1, 0, 0]` | Index and middle open |
| ✊ **Fist** | `[0, 0, 0, 0, 0]` | All fingers closed |
| 🖐 **Open Palm** | `[1, 1, 1, 1, 1]` | All fingers open |


## Hand Landmark Reference

Mediapipe detects **21 landmarks** on the hand, as shown in the image below:

![Hand Landmarks](hand-landmarks.png)



🛠 Troubleshooting

🔆 Ensure good lighting conditions for accurate detection.

🐍 If you encounter ModuleNotFoundError: No module named 'cv2', run pip install opencv-python.

📷 Check your camera permissions if the webcam is not working.

🤝 Contributing

If you wish to improve this project, feel free to fork the repository and submit a pull request. 🎯🔧

📜 License

This project is open-source and available under the MIT License.

👨‍💻 Author

Developed by Atharva Rajoba 🚀
