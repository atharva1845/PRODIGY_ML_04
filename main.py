import cv2
import mediapipe as mp
import math

mp_hands = mp.solutions.hands
hand_tracker = mp_hands.Hands(min_detection_confidence=0.5,
                              min_tracking_confidence=0.5)
draw_helper = mp.solutions.drawing_utils
def compute_angle(ptA, ptB, ptC):
    vecBA = (ptA[0] - ptB[0], ptA[1] - ptB[1])
    vecBC = (ptC[0] - ptB[0], ptC[1] - ptB[1])
    dot_prod = vecBA[0] * vecBC[0] + vecBA[1] * vecBC[1]
    magBA = math.sqrt(vecBA[0] ** 2 + vecBA[1] ** 2)
    magBC = math.sqrt(vecBC[0] ** 2 + vecBC[1] ** 2)
    cosine_val = dot_prod / (magBA * magBC + 1e-6)
    return math.degrees(math.acos(max(min(cosine_val, 1), -1)))
def is_extended(landmarks, joint1, joint2, joint3, angle_thresh=160):
    return compute_angle(landmarks[joint1], landmarks[joint2], landmarks[joint3]) > angle_thresh
def detect_hand_gesture(hand_landmarks, frame_w, frame_h):
    pts = [(int(lm.x * frame_w), int(lm.y * frame_h)) for lm in hand_landmarks.landmark]
    thumb_open = is_extended(pts, 2, 3, 4, angle_thresh=150)
    index_open = is_extended(pts, 5, 6, 8)
    middle_open = is_extended(pts, 9, 10, 12)
    ring_open = is_extended(pts, 13, 14, 16)
    pinky_open = is_extended(pts, 17, 18, 20)
    fingers = [int(thumb_open), int(index_open), int(middle_open), int(ring_open), int(pinky_open)]

    calc_dist = lambda a, b: math.hypot(a[0] - b[0], a[1] - b[1])
    scale = calc_dist(pts[0], pts[9])

    if calc_dist(pts[4], pts[8]) < 0.3 * scale and fingers[2:] == [1, 1, 1]:
        return "OK"
    if fingers == [1, 0, 0, 0, 0]:
        return "Thumbs Up"
    if fingers == [0, 1, 0, 0, 1]:
        return "Rock"
    if fingers == [1, 1, 0, 0, 1]:
        return "Yo"
    if fingers == [1, 0, 0, 0, 1]:
        return "Call Me"
    if fingers == [0, 1, 1, 1, 0]:
        return "Three"
    if fingers == [0, 1, 1, 1, 1]:
        return "Four"
    if fingers == [0, 0, 0, 0, 0]:
        return "Fist"
    if fingers == [1, 1, 1, 1, 1]:
        return "Open Palm"
    if fingers == [0, 1, 0, 0, 0]:
        return "Pointing"
    if fingers == [0, 1, 1, 0, 0]:
        return "Victory"
    if fingers == [0, 0, 1, 0, 0]:
        return "Fuck Off"
    if fingers == [0, 0, 0, 0, 1]:
        return "Susu"
    return "Unknown"
def run_gesture_recognition():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not available.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        h, w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hand_tracker.process(rgb_frame)

        gesture = "No Hand"
        if results.multi_hand_landmarks:
            for handLM in results.multi_hand_landmarks:
                draw_helper.draw_landmarks(frame, handLM, mp_hands.HAND_CONNECTIONS)
                gesture = detect_hand_gesture(handLM, w, h)
                cv2.putText(frame, gesture, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("Gesture Detector", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    run_gesture_recognition()
