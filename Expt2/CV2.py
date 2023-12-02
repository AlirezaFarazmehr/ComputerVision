import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image_path = input("Enter the path of the image: ")
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Draw and display histogram of grayscale image
plt.figure()
plt.hist(gray_image.ravel(), 256, [0, 256])
plt.title("Histogram of Grayscale Image")
plt.show()

# Draw and display histogram of color image
plt.figure()
color = ('b','g','r')
for i, col in enumerate(color):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color = col)
    plt.xlim([0, 256])
plt.title("Histogram of Color Image")
plt.show()

# Calculate the histogram equalization
equalized_image = cv2.equalizeHist(gray_image)

# Draw and display the equalized histogram
plt.figure()
plt.hist(equalized_image.ravel(), 256, [0, 256])
plt.title("Equalized Histogram of Grayscale Image")
plt.show()

# Calculate the Fourier Transform
f = np.fft.fft2(gray_image)
f_shift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(f_shift))

# Draw and display the Fourier Transform
plt.figure()
plt.imshow(magnitude_spectrum, cmap='gray')
plt.title("Fourier Transform of Grayscale Image")
plt.show()

# Save the modified images
cv2.imwrite("gray_histogram.jpg", gray_image)
cv2.imwrite("color_histogram.jpg", image)
cv2.imwrite("equalized_histogram.jpg", equalized_image)
cv2.imwrite("fourier_transform.jpg", magnitude_spectrum)

print("Images saved successfully.")