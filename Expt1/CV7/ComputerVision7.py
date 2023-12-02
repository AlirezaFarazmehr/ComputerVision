import cv2

# Load the image from the computer
image_path = input("Enter the path of the image: ")
image = cv2.imread(image_path)

# Display the original image
cv2.imshow("Original Image", image)
cv2.waitKey(0)

# Convert the image to different color models and display/save them
color_models = {
    "Grayscale": cv2.COLOR_BGR2GRAY,
    "HSV": cv2.COLOR_BGR2HSV,
    "RGB": cv2.COLOR_BGR2RGB,
    "Lab": cv2.COLOR_BGR2Lab,
    "YUV": cv2.COLOR_BGR2YUV,
}

for model_name, color_model in color_models.items():
    converted_image = cv2.cvtColor(image, color_model)

    # Display the converted image
    cv2.imshow(model_name, converted_image)
    cv2.waitKey(0)

    # Save the converted image
    save_path = f"converted_{model_name.lower()}.jpg"
    cv2.imwrite(save_path, converted_image)

cv2.destroyAllWindows()