# DeOldify

This project demonstrates how to colorize black-and-white images using a pre-trained deep learning model with OpenCV and Caffe. The model was developed by Richard Zhang et al., and it automatically adds color to grayscale images by predicting the a and b color channels in the LAB color space. This technique is useful for revitalizing old photos or generating color data from grayscale images.

## Overview
This project aims to take black-and-white (grayscale) images and convert them to color using a deep learning model. The Caffe-based model predicts the chrominance values (color) while the lightness channel is preserved from the grayscale image. This technique uses machine learning to infer the most likely colors for various regions of an image.

The process involves:
- Loading a pre-trained model that was trained on thousands of color images.
- Transforming the grayscale image to LAB color space.
- Feeding the lightness channel (*L*) into the model to predict the *a* and *b* channels (chrominance).
- Combining these channels to produce a full-color image.