import cv2
import numpy as np
from scipy import signal


def apply_filter(image, filter_type):
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply selected filter
    if filter_type == 'low-pass':
        kernel = np.ones((5, 5), np.float32) / 25
        filtered_image = cv2.filter2D(gray_image, -1, kernel)
    elif filter_type == 'high-pass':
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        filtered_image = cv2.filter2D(gray_image, -1, kernel)
    elif filter_type == 'cross-pass':
        kernel = np.array([[-1, 0, -1], [0, 4, 0], [-1, 0, -1]])
        filtered_image = cv2.filter2D(gray_image, -1, kernel)
    elif filter_type == 'non-cross-pass':
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        filtered_image = cv2.filter2D(gray_image, -1, kernel)
    elif filter_type == 'selective':
        kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        filtered_image = cv2.filter2D(gray_image, -1, kernel)
    elif filter_type == 'toothed':
        kernel = signal.windows.kaiser(20, beta=10)
        filtered_image = signal.convolve2d(gray_image, kernel, boundary='symm', mode='same')
        filtered_image = np.clip(filtered_image, 0, 255).astype(np.uint8)
    else:
        raise ValueError('Invalid filter type!')

    return filtered_image

# Load image from file
image_path = input("Enter the path of the image: ")
image = cv2.imread(image_path)

# Apply different filters
filtered_image1 = apply_filter(image, 'low-pass')
filtered_image2 = apply_filter(image, 'high-pass')
filtered_image3 = apply_filter(image, 'cross-pass')
filtered_image4 = apply_filter(image, 'non-cross-pass')
filtered_image5 = apply_filter(image, 'selective')
filtered_image6 = apply_filter(image, 'toothed')

# Display the filtered images
cv2.imshow('Original Image', image)
cv2.imshow('Low-pass Filter', filtered_image1)
cv2.imshow('High-pass Filter', filtered_image2)
cv2.imshow('Cross-pass Filter', filtered_image3)
cv2.imshow('Non-cross-pass Filter', filtered_image4)
cv2.imshow('Selective Filter', filtered_image5)
cv2.imshow('Toothed Filter', filtered_image6)

# save the filtered images
cv2.imwrite('Low-pass Filter', filtered_image1)
cv2.imwrite('High-pass Filter', filtered_image2)
cv2.imwrite('Cross-pass Filter', filtered_image3)
cv2.imwrite('Non-cross-pass Filter', filtered_image4)
cv2.imwrite('Selective Filter', filtered_image5)
cv2.imwrite('Toothed Filter', filtered_image6)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()