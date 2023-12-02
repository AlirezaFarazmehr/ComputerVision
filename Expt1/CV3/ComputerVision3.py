import cv2
import numpy as np


def add_salt_and_pepper_noise(image, probability):
    h, w = image.shape[:2]
    num_pixels = int(probability * h * w)

    # Salt noise
    salt_coords = [np.random.randint(0, i - 1, num_pixels) for i in (h, w)]
    image[salt_coords[0], salt_coords[1]] = 255

    # Pepper noise
    pepper_coords = [np.random.randint(0, i - 1, num_pixels) for i in (h, w)]
    image[pepper_coords[0], pepper_coords[1]] = 0

    return image


def add_gaussian_noise(image, mean, std_dev):
    noise = np.random.normal(mean, std_dev, image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    return noisy_image


def add_speckle_noise(image, mean, std_dev):
    noise = np.random.normal(mean, std_dev, image.shape).astype(np.uint8)
    noisy_image = image + image * noise
    return noisy_image


def add_poisson_noise(image):
    noisy_image = np.random.poisson(image).astype(np.uint8)
    return noisy_image


# Load input image
image_path = input("Enter the path of the image: ")
input_image = cv2.imread(image_path)

# Add salt and pepper noise
salt_pepper_noise_image = add_salt_and_pepper_noise(input_image.copy(), probability=0.01)
cv2.imwrite('salt_pepper_noise_image.jpg', salt_pepper_noise_image)

# Add Gaussian noise
gaussian_noise_image = add_gaussian_noise(input_image.copy(), mean=0, std_dev=50)
cv2.imwrite('gaussian_noise_image.jpg', gaussian_noise_image)

# Add speckle noise
speckle_noise_image = add_speckle_noise(input_image.copy(), mean=0, std_dev=0.05)
cv2.imwrite('speckle_noise_image.jpg', speckle_noise_image)

# Add Poisson noise
poisson_noise_image = add_poisson_noise(input_image.copy())
cv2.imwrite('poisson_noise_image.jpg', poisson_noise_image)