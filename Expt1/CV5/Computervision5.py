import cv2

# Read the image file
image_path = input("Enter the path of the image: ")
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Canny edge detection
edges = cv2.Canny(image, 100, 200)

# Save the edge image
cv2.imwrite('edges.jpg', edges)