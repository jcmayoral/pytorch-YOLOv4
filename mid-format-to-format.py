import sys
import cv2
from tqdm import tqdm

file_dict = dict()

with open(sys.argv[1], 'r') as labels:
    for l in tqdm(labels):
        tmp = l.rstrip().split(" ")
        img = tmp[0]
        mid, bcx,bcy, bcw, bch = [float(f) for f in tmp[1:]]
        cv_img = cv2.imread(img)
        h,w,c = cv_img.shape


        nx1 = int((bcx-bcw/2) * w)
        nx2 = int((bcx+bcw/2) * w)
        ny1 = int((bcy-bch/2) * h)
        ny2 = int((bcy+bch/2) * h)


        if img not in file_dict.keys():
            file_dict[img] = list()
            file_dict[img].append([nx1,ny1, nx2, ny2, mid])

        else:
            #print("key found", img)
            file_dict[img].append([nx1,ny1, nx2, ny2,mid])



with open (sys.argv[2], 'a') as new_labels:
    for key, value in tqdm(file_dict.items()):
        sentence = str()
        for detection in value:
            sentence += ",".join(map(str,detection))
            sentence += " "
        sentence = key + " " + sentence
        new_labels.write(sentence+"\n")

#print (file_dict.keys())
