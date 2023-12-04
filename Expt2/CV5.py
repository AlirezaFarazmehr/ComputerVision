from PIL import Image
import cv2

def analyze_image(image_path):
    image = Image.open(image_path)

    # Display header information
    print(f"Header: {image.format_description}")

    # Display compression information
    if image.info.get("compression"):
        compression_info = image.info["compression"]
        print(f"Compression: {compression_info}")

        # Get compression algorithm and type
        compression_algorithm = compression_info.split()[0].strip()
        compression_type = compression_info.split()[1].strip()
        print(f"Compression Algorithm: {compression_algorithm}")
        print(f"Compression Type: {compression_type}")

    print("")

# Provide the file paths of the two images
image1_path = input("Enter the path of the image1: ")
img1 = cv2.imread(image1_path)
image2_path = input("Enter the path of the image2: ")
img2 = cv2.imread(image2_path)

# Analyze the first image
analyzed_image1 = analyze_image(img1)

# Analyze the second image
analyzed_image2 = analyze_image(img2)

# Compare the header and compression information of the two images
if analyzed_image1 == analyzed_image2:
    print("The images have the same header and compression information.")
else:
    print("The images have different header and/or compression information.")