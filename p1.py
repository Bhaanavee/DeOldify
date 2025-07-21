import numpy as np
import argparse
import os
import cv2

DIR=r'/Users/bhaanaveecs/Documents/BW to Color'
PROTOTXT=os.path.join(DIR,r"For Colorisation/colorization_deploy_v2.prototxt")
POINTS=os.path.join(DIR,r"For Colorisation/pts_in_hull.npy")
MODEL=os.path.join(DIR,r"For Colorisation/colorization_release_v2.caffemodel")

if not os.path.exists(MODEL):
    print(f"Error: Model file not found at {MODEL}")
    print("Please download the required model file first")
    sys.exit(1)


ap=argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to input image")
args=vars(ap.parse_args())

print("Load model")
net=cv2.dnn.readNetFromCaffe(PROTOTXT,MODEL)
pts=np.load(POINTS)

class8=net.getLayerId("class8_ab")
conv8=net.getLayerId("conv8_313_rh")
pts=pts.transpose().reshape(2,313,1,1)
net.getLayer(class8).blobs=[pts.astype("float32")]
net.getLayer(conv8).blobs=[np.full([1,313],2.606,dtype="float32")]

image=cv2.imread(args["image"])
scaled=image.astype("float32")/255.0
lab=cv2.cvtColor(scaled,cv2.COLOR_BGR2LAB)

resized=cv2.resize(lab,(224,224))
L=cv2.split(resized)[0]
L-=50

print("Colorizing the image")
net.setInput(cv2.dnn.blobFromImage(L))
ab=net.forward()[0,:,:,:].transpose((1,2,0))

