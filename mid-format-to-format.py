import sys
import cv2

file_dict = dict()

with open(sys.argv[1], 'r') as labels:
    for l in labels:
        img, id, bcx,bcy, bcw, bch = l.rstrip().split(" ")
        cv_img = cv2.imread(img)
        w,h,c = cv_img.shape

        nx = int(float(bcx)*w)
        ny = int(float(bcy)*h)

        range_w = int(float(bcw)*w)
        range_h = int(float(bcw)*h)

        nx1 = nx - range_w//2
        ny1 = ny - range_w//2
        nx2 = nx + range_w//2
        ny2 = ny + range_w//2

        if img not in file_dict.keys():
            file_dict[img] = [nx1,ny1, nx2, ny2, id]

        else:
            #print("key found", img)
            file_dict[img].extend([nx1,ny1, nx2, ny2, id])



with open (sys.argv[2], 'a') as new_labels:
    for key, value in file_dict.items():
        sentence = ",".join(map(str,value))
        sentence = key + " " + sentence
        new_labels.write(sentence+"\n")

#print (file_dict.keys())
