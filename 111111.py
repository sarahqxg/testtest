import cv2
import unmpy as np

#create a blank image 
image = np.zeors((400,600,3), dtype=np.unit8)

#draw a rectngle
cv2.rectangle(image,(50,50),(200,150),(0,255,0), thiclness=2)

#draw a circle
cv2.circle(image,(300,100),30,(0,0,255), thickness=-1)

cv2.imshow('OpenCV Exanple', image)

cv2.waitkey(0)
cv2.destroyAllWindows()
