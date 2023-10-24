import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height= int(cap.get(4))
    hsv =cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 63 105 204
    # 0 0 255
    lower_red = np.array([50,50,90])
    upper_red = np.array([130,255,255])
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130,255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result =cv2.bitwise_and(frame, frame, mask=mask)


#     image = np.zeros(frame.shape, np.uint8)
#     # img = cv2.line(frame, (0,0),(width, 0), (255,0,0), 20)
#     # img = cv2.line(img, (width,0),(width, height), (255,0,0), 20)
#     # img = cv2.line(img, (width, height),(0,height), (255,0,0), 20)
#     # img = cv2.line(img, (0,height),(0, 0), (255,0,0), 20)
#     # img = cv2.rectangle(frame, (100,100),(200,200),(128,128,128),5)
#     # img = cv2.circle(frame, (300,300), 60, (0,0,255),-1)
#     # font = cv2.FONT_HERSHEY_SIMPLEX
#     # img = cv2.putText(frame, 'python', (100, height-10), font, 4, (0,0,255), 5, cv2.LINE_AA)
#     # smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
#     # image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
#     # image[height//2:, :width//2] =smaller_frame
#     # image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
#     # image[height//2:, width//2:] = smaller_frame
#     # cv2.imshow("frame", image)
    cv2.imshow("frame", result)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()