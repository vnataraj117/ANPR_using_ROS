#!/usr/bin/env python

import imutils
import numpy as np
import pytesseract
from PIL import Image
import rospy, cv2, cv_bridge
import smtplib
import sys, time, math
from sensor_msgs.msg import Image
import numpy


def main(msg):
    #--- Capture the videocamera (this may also be a video or a picture)
    cap = cv_bridge.CvBridge()



    #-- Font for the text in the image
    #font = cv2.FONT_HERSHEY_PLAIN


    #-- Read the camera frame
    img = cap.imgmsg_to_cv2(msg,desired_encoding='bgr8')
    img = cv2.resize(img, (620,480) )


    #-- Convert in gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
    gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
    edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE,              cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
    screenCnt = None
    for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018 * peri, True)
            if len(approx) == 4:
                  screenCnt = approx
                  break
    if screenCnt is None:
               detected = 0
               print ("No contour detected")
    else:
               detected = 1
    if detected == 1:
               print "detected"
               cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
               mask = np.zeros(gray.shape,np.uint8)
               new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
               new_image = cv2.bitwise_and(img,img,mask=mask)
               (x, y) = np.where(mask == 255)
               (topx, topy) = (np.min(x), np.min(y))
               (bottomx, bottomy) = (np.max(x), np.max(y))
               Cropped = gray[topx:bottomx+1, topy:bottomy+1]
               tessdata_dir_config = r'--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata/"'
               text = pytesseract.image_to_string(Cropped, lang='eng',config=tessdata_dir_config)
               print("Detected Number is:",text)
               #cv2.imshow('bottom_camera', Cropped)
               #cv2.waitKey(0)
    cv2.imshow("Frame", img)
    
    



    #--- use 'q' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()

def land():
	print "finding Number Plate"
	image_sub = rospy.Subscriber('/realsense/color/image_raw', Image, main)

	

if __name__ == '__main__':
		cv2.destroyAllWindows()
		rospy.init_node('landing')
		land()
		rospy.spin()
