import cv2
import numpy as np
import os
from PIL import Image


def detectVideo(fileName):
    #  https://pjreddie.com/darknet/yolo/ to download weight file
    #!git clone https://github.com/pjreddie/darknet to download cfg file
    #https://github.com/pjreddie/darknet/blob/master/data/coco.names
    net = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')

    classes=[]
    with open('coco.names','r') as f:
        classes = f.read().splitlines()

    print(classes)

    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    #fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    out = cv2.VideoWriter("outputYOLO.mp4", fourcc, 5.0, (1280,720))

    #from video
    #cap = cv2.VideoCapture('C:/Users/Admin/guiTest/1.avi')
    cap = cv2.VideoCapture(fileName)


    #1/255 image normailzation 
    #416,416 image resize
    #swapRB change position red and blue (rgb to bgr)

    while True:
        _, img= cap.read()
        height, width, _ = img.shape
        blob = cv2.dnn.blobFromImage(img, 1/255,  (416,416), (0,0,0), swapRB=True, crop=False)

        # for b in blob:
        #     for n, img_blob in enumerate(b):
        #         cv2.imshow()

        #to set input 
        net.setInput(blob)

        #get output layers names
        output_layers_names = net.getUnconnectedOutLayersNames()

        #get function layerOutputs provided by layer names
        layerOutputs = net.forward(output_layers_names)

        boxes=[]
        confidences = []
        class_ids =[]

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5 :
                    center_x = int(detection[0]*width)
                    center_y = int(detection[1]*height)
                    w = int(detection[2]*width)
                    h = int(detection[3]*height)

                    x = int(center_x - w/2)
                    y = int(center_y - h/2)

                    boxes.append([x,y,w,h])
                    confidences.append((float(confidence)))
                    class_ids.append(class_id)

        print(len(boxes))

        #0.5 is same with confidence threshold
        #0.4 is max suppression
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        font = cv2.FONT_HERSHEY_PLAIN
        #colors = np.random.uniform(0,255,size=(len(boxes), 3))
        if len(indexes)>0:
            for i in indexes.flatten():
                
                x,y,w,h = boxes[i]
                h_img= img.shape[0] 
                w_img= img.shape[1] 
                win = np.zeros((h_img, w_img,3),np.uint8)
                label = str(classes[class_ids[i]])
                if label == 'person':
                    confidence = str(round(confidences[i],2))
                    #color = colors[i]
                    #cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                    #cv2.putText(img, label , (x,y+20), font, 2, (255,255,255), 2)
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2) 
                    cv2.rectangle(win, (x,y), (x+w, y+h), (200,200,250), -1)            
                    cv2.putText(img, label , (x,y+10), font, 1, (0,0,255), 2)
                    img = cv2.addWeighted(img, 0.8, win,0.4, 0)
        
        #esc key
        cv2.imshow('Image', img)
        
        imageWrite = cv2.resize(img, (1280,720))
        #imgOut = Image.fromarray(out)
        out.write(imageWrite)
        key = cv2.waitKey(1)
        if key==27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    os.system('python playDetectedVideo.py')
        
