import cv2
import numpy as np
image1_path = input("Enter the path of the image1: ")
img1 = cv2.imread(image1_path)
image2_path = input("Enter the path of the image2: ")
img2 = cv2.imread(image2_path)
image3_path = input("Enter the path of the image3: ")
img3 = cv2.imread(image3_path)
image4_path = input("Enter the path of the image4: ")
img4 = cv2.imread(image4_path)

gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
gray_img4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(gray_img1, None)
flann = cv2.FlannBasedMatcher()

keypoints2, descriptors2 = orb.detectAndCompute(gray_img2, None)
matches = flann.knnMatch(descriptors1, descriptors2, k=2)
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)
similarity_score = len(good_matches) / len(matches) * 100
print("Similarity score for image 2: ", similarity_score)

keypoints3, descriptors3 = orb.detectAndCompute(gray_img3, None)
matches = flann.knnMatch(descriptors1, descriptors3, k=2)
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)
similarity_score = len(good_matches) / len(matches) * 100
print("Similarity score for image 3: ", similarity_score)

keypoints4, descriptors4 = orb.detectAndCompute(gray_img4, None)
matches = flann.knnMatch(descriptors1, descriptors4, k=2)
good_matches = []
for m, n in matches:
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)
similarity_score = len(good_matches) / len(matches) * 100
print("Similarity score for image 4: ", similarity_score)