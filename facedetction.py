import cv2

cap = cv2.VideoCapture(0)  

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()


window_name = 'Video Capture'


cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

while True:

    ret, frame = cap.read()

   
    if not ret:
        print("Error: Failed to capture frame.")
        break

    cv2.imshow(window_name, frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

