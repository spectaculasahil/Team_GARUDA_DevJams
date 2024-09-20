import cv2


cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Error: Could not open video capture")
else:
    print("OpenCV is working. Press 'q' to exit.")


while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Webcam Test', frame)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Failed to capture video frame")
        break


cap.release()
cv2.destroyAllWindows()
