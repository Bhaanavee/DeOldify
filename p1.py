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
