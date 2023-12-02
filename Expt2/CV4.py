import cv2
import numpy as np

# Step 1: Import the necessary libraries

# Step 2: Load the images from the computer
image1_path = input("Enter the path of the image1: ")
img1 = cv2.imread(image1_path)
image2_path = input("Enter the path of the image2: ")
img2 = cv2.imread(image2_path)
image3_path = input("Enter the path of the image3: ")
img3 = cv2.imread(image3_path)
image4_path = input("Enter the path of the image4: ")
img4 = cv2.imread(image4_path)

# Step 3: Convert the images to grayscale
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
gray_img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)

# Step 4: Apply histogram matching to match the histograms of the second, third, and fourth images with the first image
matched_img2 = cv2.createCLAHE().apply(gray_img2)
matched_img3 = cv2.createCLAHE().apply(gray_img3)
matched_img4 = cv2.createCLAHE().apply(gray_img4)

# Step 5: Calculate the similarity score for each image by comparing it with the first image
similarity_score2 = cv2.compareHist(matched_img2, gray_img1, cv2.HISTCMP_CORREL)
similarity_score3 = cv2.compareHist(matched_img3, gray_img1, cv2.HISTCMP_CORREL)
similarity_score4 = cv2.compareHist(matched_img4, gray_img1, cv2.HISTCMP_CORREL)

# Step 6: Print the similarity scores for each image
print("Similarity score for the second image: ", similarity_score2)
print("Similarity score for the third image: ", similarity_score3)
print("Similarity score for the fourth image: ", similarity_score4)