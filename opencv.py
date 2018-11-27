
import cv2
 
def face(name):
    print '正在处理'
 
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    count = 0
    img = cv2.imread(name)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        count+=1
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),4)
        font = cv2.FONT_HERSHEY_SIMPLEX
 
        roi_gray = gray[y:y+h/2, x:x+w]
        roi_color = img[y:y+h/2, x:x+w]
 
 
    cv2.imwrite("face_detected_1.jpg", img)     #保存已经生成好的图片
    print count
    return count    
