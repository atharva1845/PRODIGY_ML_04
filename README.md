**✋ Hand Gesture Recognition using Mediapipe**


Overview

Hand Gesture Recognition is a crucial technology in human-computer interaction, enabling touchless control, sign language interpretation, and immersive experiences in AR/VR applications. This project leverages OpenCV and Mediapipe to accurately detect and classify hand gestures from image or video data in real time.

By using Mediapipe’s advanced hand-tracking model, this system can recognize multiple gestures, making it suitable for applications such as virtual controls, assistive technologies, and gaming interfaces.

Features
Real-time hand gesture detection using a webcam feed.
Multi-gesture support including thumbs up, OK sign, fist, rock sign, victory sign, and more.
Efficient hand tracking powered by Mediapipe, providing 21 hand landmarks for precise recognition.
Lightweight implementation that runs on standard hardware with minimal computational requirements.
Easy integration into existing applications for gesture-based control.

Installation
To use this project, install the required dependencies:

  ```
pip install opencv-python mediapipe numpy
  ```
Ensure Python and pip are installed before running the command.

Usage
To start the hand gesture recognition system, execute the following command:

  ```
python hand_gesture_recognition.py
  ```
This will launch the webcam and begin detecting hand gestures in real time.



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


Hand Landmark Reference
Mediapipe detects **21 unique landmarks** on the hand, which serve as reference points for identifying gestures. The following diagram illustrates these landmark positions:

![Hand Landmarks](hand-landmarks.png)



Applications
This system has a wide range of applications, including but not limited to:

-Sign Language Recognition: Assisting communication for individuals with speech impairments.
-Touchless Control Systems: Enabling interactions in AR/VR environments.
-Gaming and Entertainment: Providing gesture-based controls for immersive experiences.
-Automotive Industry: Implementing hands-free control for in-car systems.
-Healthcare and Assistive Tech: Supporting rehabilitation and accessibility applications.

Troubleshooting
-Lighting Conditions: Ensure adequate lighting to improve gesture recognition accuracy.
-Module Not Found Error: If encountering ModuleNotFoundError: No module named 'cv2', install OpenCV using pip install opencv-python.
-Webcam Issues: Check camera permissions if the video feed does not appear.

Contributing
This is an open-source project, and contributions are welcome. If you have ideas for improvements or additional gesture recognition capabilities, feel free to fork the repository and submit a pull request.

License
This project is licensed under the MIT License, allowing free use, modification, and distribution.

👨‍💻 Author

Developed by Atharva Rajoba 🚀
