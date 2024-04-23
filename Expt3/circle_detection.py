import cv2
import numpy as np


# Function to find and draw circles in the image
def find_and_draw_circles(image_path):
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and help the circle detection
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Use Circles to detect circles in the image
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=100, param2=30, minRadius=10, maxRadius=100
    )

    # If circles are found, draw them
    if circles is not None:
        # Convert the circle coordinates to integers
        circles = np.uint16(np.around(circles))

        for i in circles[0, :]:
            # Draw the outer circle
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

    # Display and save the result
    cv2.imshow('Detected Circles', img)
    cv2.imwrite('detected_circles_output.jpg', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Get the image path from the user
image_path = input("Enter the path of the image: ")

# Find and draw circles in the image
find_and_draw_circles(image_path)
