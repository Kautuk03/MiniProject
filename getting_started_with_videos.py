import cv2
import datetime
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#format: cv2.VideoWriter('filename.avi',videowriter variable,fps,(x dimen,y dimention))
print(cap.isOpened())
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 3000)
cap.set(4,3000)
print("After set function: ")
print(cap.get(3))
print(cap.get(4))
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_COMPLEX
        out.write(frame)
        #converting from BGR colour to Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #seeing the output in greyscale(write grey intead of frame)
        cv2.imshow('frame', frame)

        #breaking the videocapture by pressing the button 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
