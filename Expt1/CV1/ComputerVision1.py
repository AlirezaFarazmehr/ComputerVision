import cv2

def read_image():
    image_path = input("Enter the path of the image: ")  # Get the path of the image from the user
    image = cv2.imread(image_path)  # Read the image using OpenCV
    return image

def save_image(image, file_name):
    cv2.imwrite(file_name, image)  # Save the image to the specified file name

def show_image(image, window_name):
    cv2.imshow(window_name, image)  # Display the image in a separate window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convert_to_binary(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert the image to gray-scale
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # Threshold the gray-scale image to binary
    return binary

def main():
    image = read_image()

    save_binary = input("Do you want to save the binary image? (y/n): ")
    save_gray = input("Do you want to save the gray-scale image? (y/n): ")
    save_color = input("Do you want to save the color image? (y/n): ")

    if save_binary.lower() == 'y':
        binary_image = convert_to_binary(image)
        save_image(binary_image, "binary_image.png")
        show_image(binary_image, "Binary Image")

    if save_gray.lower() == 'y':
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        save_image(gray_image, "gray_image.png")
        show_image(gray_image, "Gray Scale Image")

    if save_color.lower() == 'y':
        show_image(image, "Color Image")
        save_image(image, "color_image.png")

if __name__ == '__main__':
    main()