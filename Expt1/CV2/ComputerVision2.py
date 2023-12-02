import cv2

def adjust_contrast(image, contrast_factor):
    # Adjust contrast using cv2.convertScaleAbs
    adjusted_image = cv2.convertScaleAbs(image, alpha=contrast_factor, beta=0)
    return adjusted_image

# Load the input image
image_path = input("Enter the path of the image: ")
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Reduce the contrast for gray image
reduced_gray_image = adjust_contrast(gray_image, 0.5)

# Increase the contrast for gray image
increased_gray_image = adjust_contrast(gray_image, 1.5)

# Reduce the contrast for color image
reduced_color_image = adjust_contrast(image, 0.5)

# Increase the contrast for color image
increased_color_image = adjust_contrast(image, 1.5)

# Save the output images
cv2.imwrite("reduced_gray_image.jpg", reduced_gray_image)
cv2.imwrite("increased_gray_image.jpg", increased_gray_image)
cv2.imwrite("reduced_color_image.jpg", reduced_color_image)
cv2.imwrite("increased_color_image.jpg", increased_color_image)