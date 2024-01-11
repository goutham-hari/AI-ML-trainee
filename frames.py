import cv2
import os
import random

video_path = 'video.mp4'
cap = cv2.VideoCapture(video_path)

fps = int(cap.get(cv2.CAP_PROP_FPS))

output_directory = 'screenshots'
os.makedirs(output_directory, exist_ok=True)

cv2.namedWindow('Random Screenshot and Video', cv2.WINDOW_NORMAL)

try:
    while cap.isOpened():
  
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Random Screenshot and Video', frame)

        if random.random() < 0.10:  
            screenshot_path = os.path.join(output_directory, f'screenshot_{int(cap.get(cv2.CAP_PROP_POS_FRAMES))}.png')
            cv2.imwrite(screenshot_path, frame)
            print(f'Saved screenshot: {screenshot_path}')

        
        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
   
    cap.release()
    cv2.destroyAllWindows()
