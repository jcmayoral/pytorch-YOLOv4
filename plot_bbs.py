import cv2
import sys
import matplotlib.pyplot as plt

fig = plt.Figure()
plt.show(block=False)
with open(sys.argv[1],"r") as file:
    for image_info in file:
        split_string = image_info.rstrip().split(" ")
        img_path = split_string[0].rstrip()
        bbs = split_string[1:]
        print(img_path)
        img = cv2.imread(img_path)
        for bb in bbs:
            x1,y1,x2,y2, cl = bb.rstrip().split(",")
            print(x1,y1, bbs)
            img = cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (255,0,0),4)
        plt.imshow(img)
        plt.pause(0.1)
