import cv2

# Load the image
image_path = input("Enter the path of the image: ")
image = cv2.imread(image_path)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Save the blurred image
cv2.imwrite('blurred_image.jpg', blurred_image)