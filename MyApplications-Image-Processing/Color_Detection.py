import cv2
import numpy as np
import time

#find the center of an object
def center(contours):

    # calculate moments for each contour
    for c in contours:
        M = cv2.moments(c)
        
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        else:
            cX, cY = 0, 0
        tempStr = str(cX) + ", " + str(cY)
        cv2.circle(frame, (cX, cY), 1, (0, 0, 0), -1) #make a dot at the center of the object 
        cv2.putText(frame, tempStr, (cX - 25, cY - 25),cv2.FONT_HERSHEY_TRIPLEX, 0.4, (0, 0, 0), 1) #print the coordinates on the image_process

        #open text for starting coordinates
        coordinate = open("/image_process/coord.txt", "w")
        coordinate.write("First Impression: {}\n".format(tempStr))
        coordinate.close()

#get the region of interest
def find_ROI(frame):
    image = frame.copy()

    #change to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Get binary image_process
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    #create structural element
    struc_ele = np.ones((5, 5), np.uint8)

    #Use Open Morphology
    img_open = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, struc_ele, iterations = 1)

    #find contours
    ctrs, _ = cv2.findContours(img_open.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # sort contours
    sorted_ctrs = sorted(ctrs, key=lambda ctr: cv2.boundingRect(ctr)[1])

    for i, ctr in enumerate(sorted_ctrs):
        # Get bounding box
        x, y, w, h = cv2.boundingRect(ctr)

        # Getting ROI
        roi = image[y:y + h, x:x + w]
 

cap = cv2.VideoCapture(0) #open camera
coordinate = open("C:\Users\Oprah\Desktop\Kodlama Egzersizleri\image\coord.txt","a") #append the coordinates

if __name__ == "__main__":
    while True:
        _, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        find_ROI(frame)
        

        #Create kernel to use in filter
        kernel = np.ones((5, 5), np.uint8)

        #Create filter for yellow
        lower_yellow = np.array([15, 100, 100]) #Lower boundary values for HSV
        upper_yellow = np.array([30, 255, 255]) #Upper boundary values for HSV

        yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow) # Threshold the HSV image_process to get only yellow colors
        opening_y = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel, iterations = 2) #Use morphology open to rid of false pos and false neg (noise)
        result_y = cv2.bitwise_and(frame, frame, mask = opening_y) #bitwise and the opening filter with the original frame 




       
        
  
        #Tracking the color yellow
        contours, _ = cv2.findContours(opening_y, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for y_pix, contour in enumerate (contours):
                area = cv2.contourArea (contour)
                if (area > 300):
                        center(contours)
                        x, y, w, h = cv2.boundingRect(contour)
                        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                        cv2.putText(frame, "Yellow", (x, y), cv2.FONT_HERSHEY_TRIPLEX, 0.7, (0, 255, 255))
                              
                        #create date with time
                        ms1=int(round(time.time())) 
                        local_time = time.ctime(ms1)
                        
                        coordinate.write("Coordinates and Time : {} , {} , {}\n".format(x,y,local_time))

        #show frames
        cv2.imshow("Detection and Coordinates", frame)
        cv2.imshow("Yellow Seen ", result_y)

        #esc for escape
        key = cv2.waitKey(1)
        if key == 27: 
            
            coordinate.close()

            break

cap.release()
cv2.destroyAllWindows()
