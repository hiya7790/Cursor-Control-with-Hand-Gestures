import cv2
import mediapipe as mp
import pyautogui
import time
import math

model_path = "hand_landmarker.task"

options = mp.tasks.vision.HandLandmarkerOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=model_path),
    running_mode=mp.tasks.vision.RunningMode.IMAGE,
    num_hands=1,
    min_hand_detection_confidence=0.7
)
cap = cv2.VideoCapture(0)

#gesture time control
click_start_time = None 
click_times = []
click_cooldown = 0.5 
scroll_mode = False
freeze_cursor = False


screen_w, screen_h = pyautogui.size()
print("\n hand mouse control ,")
prev_screen_x, prev_screen_y=0,0 
with mp.tasks.vision.HandLandmarker.create_from_options(options) as landmarker:


    
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame")
            break
        frame = cv2.flip(frame, 1)
        rgb_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        result = landmarker.detect(rgb_image)
        
        if result.hand_landmarks:
            h, w, c = frame.shape
            for hand_landmarks in result.hand_landmarks:
                # Draw landmarks
                for landmark in hand_landmarks:
                    x = int(landmark.x * w)
                    y = int(landmark.y * h)
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

                # Get finger tips
                thumb_tip = hand_landmarks[4]
                index_tip = hand_landmarks[8]
                middle_tip = hand_landmarks[12]
                ring_tip = hand_landmarks[16]
                pinky_tip = hand_landmarks[20]     
            
                fingers = [
                    1 if hand_landmarks[tip].y < hand_landmarks[tip - 2].y else 0
                    for tip in [8, 12, 16, 20]
                ]
                # distance btwn thumb and index
                dist=math.hypot(thumb_tip.x - index_tip.x, thumb_tip.y - index_tip.y)
                if dist < 0.06:
                    if not freeze_cursor: 
                        freeze_cursor=True
                        click_times. append(time. time())

                        #double click check 
                        if len(click_times)>=2 and click_times[-1]-click_times[-2]<0.4: 
                            pyautogui.doubleClick()
                            cv2.putText(frame, "Double Click", (10, 50), cv2.FONT_HERSHEY_SIMPLEX ,1, (0,255,255),2)
                        else:
                            pyautogui.click()
                            cv2.putText(frame, "Single Click", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,0),2)
                else:
                    if freeze_cursor:
                        time.sleep(0.1) 
                    freeze_cursor=False

                #move cursor by index_finger 
                if not freeze_cursor:
                    screen_x= int(index_tip.x *screen_w)
                    screen_y=int(index_tip.y * screen_h)
                    pyautogui.moveTo(screen_x, screen_y, duration=0.05) 
                    prev_screen_x,prev_screen_y=screen_x, screen_y

                #scroll mode 
                if sum(fingers)==4: 
                    scroll_mode=True
                else:
                    scroll_mode=False 

                    #scroll actions 
                    if scroll_mode:
                        if index_tip.y<0.4: 
                            pyautogui.scrol1(60)
                            cv2. putText (frame, "Scroll up", (10, 90), cv2. FONT_HERSHEY_SIMPLEX, 1,(0,255, 0), 2)
                        elif index_tip.y>0.6:
                            pyautogui.scroll(-60)
                            cv2. putText (frame, "scroll down", (10,90), cv2. FONT_HERSHEY_SIMPLEX, 1,(0,0, 255), 2)



        cv2.imshow("live video", frame)
        if cv2.waitKey(1) == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
