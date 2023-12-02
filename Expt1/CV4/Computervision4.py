import cv2
import numpy as np
import random

# Load the image
image_path = input("Enter the path of the image: ")
img = cv2.imread(image_path)

# Add salt and pepper noise
def salt_pepper_noise(image, probability):
    height, width = image.shape[:2]
    noisy_image = np.copy(image)
    num_pixels = int(probability * height * width)
    for _ in range(num_pixels):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        # Set random noise values (black or white)
        if random.random() < 0.5:
            noisy_image[y][x] = [0, 0, 0]  # Set black pixel
        else:
            noisy_image[y][x] = [255, 255, 255]  # Set white pixel
    return noisy_image

noisy_img = salt_pepper_noise(img, 0.05)  # Add noise with 5% probability

# Apply Median Filter to remove salt and pepper noise
filtered_img = cv2.medianBlur(noisy_img, 3)

# Save the output image
cv2.imwrite('output_image.jpg', filtered_img)
cv2.imwrite('output_noisyimage.jpg', noisy_img)
# Display the images
cv2.imshow('Noisy Image', noisy_img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()