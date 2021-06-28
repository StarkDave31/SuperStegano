import numpy as np
import cv2
import argparse
import matplotlib
import matplotlib.pyplot as plt
from convolution import convolution
from gaussian_smoothing import gaussian_blur
import pandas as pd


def sobel_edge_detection(image, filter, verbose=False):
    new_image_x = convolution(image, filter, verbose)

    if verbose:
        plt.imshow(new_image_x, cmap='gray')
        plt.title("Horizontal Edge")
        plt.show()

    new_image_y = convolution(image, np.flip(filter.T, axis=0), verbose)

    if verbose:
        plt.imshow(new_image_y, cmap='gray')
        plt.title("Vertical Edge")
        plt.show()

    gradient_magnitude = np.sqrt(np.square(new_image_x) + np.square(new_image_y))

    res=np.mean(gradient_magnitude)

    ret, thresh1 = cv2.threshold(gradient_magnitude, res, 255, cv2.THRESH_BINARY)


    cv2.imshow('Binary Threshold', thresh1)

    df = pd.DataFrame (thresh1)

    filepath = 'finData.xlsx'

    df.to_excel(filepath, index=False)

    # De-allocate any associated memory usage
    if cv2.waitKey(0) & 0xff == 27:
	    cv2.destroyAllWindows()

    
    gradient_magnitude *= 255.0 / gradient_magnitude.max()

    if verbose:
        plt.imshow(gradient_magnitude, cmap='gray')
        plt.title("Gradient Magnitude")
        plt.show()
    
    return thresh1


if __name__ == '__main__':
    filter = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="Path to the image")
    args = vars(ap.parse_args())

    image = cv2.imread(args["image"])
    image = gaussian_blur(image, 9, verbose=True)
    sobel_edge_detection(image, filter, verbose=True)
    
    
    
