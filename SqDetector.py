import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib.pyplot as plt
from config import *

def angle(p1, p2, p3):
    """Calcule l'angle entre 3 points"""
    v1 = p1 - p2
    v2 = p3 - p2
    cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return np.degrees(np.arccos(cos_theta))

def count_rect(contours, img):
    square_count = 0
    squares_pts = []

    for i, cnt in enumerate(contours):
        # print("ok contours")
        print("-----------------------------------")
        area = cv2.contourArea(cnt)
        print(f"area-{i} = {area}")
        if area < MIN_AREA_ACCEPTED:  # filtre bruit
            continue

        epsilon = 0.01 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        print("epsilon = ", epsilon)
        print("approx = ", approx)
        # print("convex contour = ", cv2.isContourConvex(approx))

        canvas = np.zeros_like(img)  # image noire même taille

        cv2.drawContours(canvas, [cnt], -1, (255, 255, 255), 2)

        # cv2.imshow(f"Contour {i}", canvas)
        # cv2.waitKey(0)
        # plt.figure()
        # plt.title(f"contour {i}")
        # plt.imshow(canvas)
        # plt.show()

        if len(approx) == 4 and cv2.isContourConvex(approx):

            pts = approx.reshape(-1, 2)

            # calcul des angles
            angles = []
            for i in range(4):
                p1 = pts[i]
                p2 = pts[(i+1) % 4]
                p3 = pts[(i+2) % 4]
                angles.append(angle(p1, p2, p3))
            print("angles = ", angles)

            # vérifier angles ~ 90°
            if all(MIN_DEG < a < MAX_DEG for a in angles):

                x, y, w, h = cv2.boundingRect(approx)
                ratio = w / float(h)
                print("ratio = ", ratio)

                if MIN_RAT < ratio < MAX_RAT:  # tolérance large

                    square_count += 1
                    squares_pts.append(cnt)
                    # cv2.drawContours(img, [approx], -1, (0,255,0), 3)
    return square_count, squares_pts

def contourDetection(img):

    # Conversion to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blurr
    blur = cv2.GaussianBlur(gray, (3,3), 0)

    # Find Canny edges
    edged = cv2.Canny(blur, LOW_THRESH, LOW_THRESH*RATIO )
    # cv2.imshow('Canny', edged)
    
    kernel = np.ones((3,3), np.uint8)
    
    edged = cv2.dilate(edged, kernel, iterations=1)
    edged = cv2.erode(edged, kernel, iterations=1)

    # Finding Contours
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    #cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
    # print("Number of Contours found = " + str(len(contours)))
    # print("Contour shape : ", contours[0].shape)

    # for i, cnt in enumerate(contours):
    #     canvas = np.zeros_like(img)  # image noire même taille

    #     cv2.drawContours(canvas, [cnt], -1, (255, 255, 255), 2)

    #     # cv2.imshow(f"Contour {i}", canvas)
    #     # cv2.waitKey(0)
    #     plt.figure()
    #     plt.title(f"contour {i}")
    #     plt.imshow(canvas)
    #     plt.show()

    # cv2.destroyAllWindows()

    nbr_sq, rects = count_rect(contours, img)

     # Draw all contours (i.e -1)
    # cv2.drawContours(img, rects, -1, (0, 255, 0), 3)


    # cv2.putText(img, f"Squares: {nbr_sq}", (20,40),
    #             cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    # cv2.namedWindow('Contours', cv2.WINDOW_NORMAL)
    # cv2.imshow('Contours', img)


    return contours, rects, nbr_sq
