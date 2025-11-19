import cv2
from deepface import DeepFace
import pyttsx3
# Load video from webcam
cap = cv2.VideoCapture(0)
last_emotion=None
engine=pyttsx3.init()

while True:
    key, img = cap.read()
    # Analyze emotion
    results = DeepFace.analyze(img, actions=['emotion'], enforce_detection=False)

    # Display emotion on frame
    emotion = results[0]['dominant_emotion']
    if emotion!=last_emotion:
        engine.say("your emotion is")
        engine.say(emotion)
        engine.runAndWait()

    cv2.putText(img, f'Emotion: {emotion}', (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow("Emotion Recognition", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()