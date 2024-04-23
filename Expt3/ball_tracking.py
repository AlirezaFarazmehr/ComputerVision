import cv2
import numpy as np

def detect_ball(frame):
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper HSV values for the ball color
    lower_color = np.array([15, 100, 100])
    upper_color = np.array([35, 255, 255])

    # Threshold the frame to extract the ball
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Perform morphological operations to reduce noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any contours are found
    if contours:
        # Find the contour with the maximum area (the ball)
        max_contour = max(contours, key=cv2.contourArea)

        # Get the bounding box of the ball
        x, y, w, h = cv2.boundingRect(max_contour)

        # Draw a rectangle around the ball
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame

def main():
    # Ask the user for the video path
    video_path = input("Enter the path of the video file (e.g., your_video.mp4): ")

    # Open a video capture object
    cap = cv2.VideoCapture(video_path)

    # Check if the video capture object is opened successfully
    if not cap.isOpened():
        print("Error: Unable to open the video file.")
        return

    # Get video properties
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Define the codec and create VideoWriter object to save the output video
    out = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Detect and track the ball in the current frame
        processed_frame = detect_ball(frame)

        # Save the processed frame to the output video
        out.write(processed_frame)

        # Display the frame with the detected ball
        cv2.imshow('Ball Tracking', processed_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release the video capture and writer objects
    cap.release()
    out.release()

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
