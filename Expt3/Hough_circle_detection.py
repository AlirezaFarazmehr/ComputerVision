import time

import cv2
import numpy as np


def detect_circles_Hough():
    # Get the image path from the user
    image_path = input("Enter the path to the image: ")

    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (15, 15), 2)

    # Detect edges using Canny
    edges = cv2.Canny(blurred, 30, 100)

    # Use Hough Transform to detect circles
    circles = cv2.HoughCircles(
        edges,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=50,
        param1=50,
        param2=25,
        minRadius=10,
        maxRadius=50  # Reduce maxRadius for smaller circles
    )

    # If at least one circle (football) is found
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        # Draw the detected circles
        for (x, y, r) in circles:
            cv2.circle(image, (x, y), r, (0, 255, 0), 4)  # Draw a circle with green border

        # Display the image containing the detected circles
        cv2.imshow("Detected circles", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Save the image with a unique filename based on the current timestamp
        timestamp = int(time.time())
        output_filename = f"Detected_Circles_{timestamp}.jpg"
        cv2.imwrite(output_filename, image)
        print(f"Image saved as {output_filename}")
    else:
        print("No circles detected.")


# Call the function
detect_circles_Hough()
