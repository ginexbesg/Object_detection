import cv2
import numpy as np





def detect(fileName):
        net = cv2.dnn.readNet('yolov3.weights','yolov3.cfg')

        classes=[]
        with open('coco.names','r') as f:
            classes = f.read().splitlines()

        print(classes)

        img= cv2.imread(fileName)
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

        for i in indexes.flatten():
            x,y,w,h = boxes[i]
            h_img= img.shape[0] 
            w_img= img.shape[1] 
            win = np.zeros((h_img, w_img,3),np.uint8)
            #print(win.shape)
            #print(img.shape)
            #print(h_img)
            #print(w_img)
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i],2))
            #color = colors[i]
            
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2) 
            cv2.rectangle(win, (x,y), (x+w, y+h), (200,200,250), -1)            
            cv2.putText(img, label , (x,y+10), font, 1, (0,0,255), 2)
            img = cv2.addWeighted(img, 0.8, win,0.4, 0)

        print(indexes.flatten())

        cv2.imshow('Image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

