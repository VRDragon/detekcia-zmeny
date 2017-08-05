import cv2
from time import gmtime,strftime
backsub = cv2.BackgroundSubtractorMOG()
capture = cv2.VideoCapture(0)
pocet    =0
if capture:
  while True:
    ret, frame = capture.read()
    if ret:
        pocetpred=pocet
        pocet = 0
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fgmask = backsub.apply(gray, None, 0.005)
        contours, hierarchy = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
        try: hierarchy = hierarchy[0]
        except: hierarchy = []
        for contour, hier in zip(contours, hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            if w > 80 and h > 120:
                    cv2.rectangle(gray, (x,y), (x+w,y+h), (255, 0, 0), 2)
                    x1 = w/2      
                    y1 = h/2
                    cx = x+x1
                    cy = y+y1
                    pocet = pocet+1
                    centroid = (cx,cy)
                    cv2.circle(gray,(int(cx),int(cy)),2,(0,0,255),-1)                        
            #cv2.imshow('FGMASK', fgmask)
        cv2.putText(frame, str(pocet),(10,200), cv2.FONT_HERSHEY_SIMPLEX,2, (0, 0, 255), 1, True)
        if pocetpred != pocet :
            print ("Pohyb na zázname bol v èase "+strftime("%Y-%m-%d %H:%M:%S", gmtime())+"objekt"+str(pocet))
        cv2.imshow('Output', gray)
    key = cv2.waitKey(10)
    if key == ord('q'):
            break
