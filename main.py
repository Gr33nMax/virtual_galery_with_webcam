import cv2, time

video = cv2.VideoCapture(1)

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 15.0, (640, 480))

numframes = 0

while True:
    numframes += 1
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # out.write(frame)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27:  # press ESC key
        break
    cv2.imwrite(f'img_{numframes}.png', frame)
    time.sleep(0.5)

video.release()
cv2.destroyAllWindows()
