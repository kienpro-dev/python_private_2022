import numpy as np
import matplotlib as mpl
import random

import cv2

# image = cv2.imread('sample.png', cv2.IMREAD_UNCHANGED)
# print(type(image))

image = cv2.imread('sample.png', cv2.IMREAD_COLOR)
# cv2.imshow('Picture 1', image)
# cv2.waitKey()
# cv2.destroyAllWindows()

img = cv2.imread('sample.png')
# px = img[150,150]
# print(px)

# img[150,150] = [255,255,255]
# print(img[150,150])

# print(image.shape)

# b,g,r = cv2.split(image)
# img = cv2.merge((b,g,r))
# b = image[:,:,0]
# g = image[:,:,1]
# r = image[:,:,2]

khung = np.zeros((300, 300, 3), dtype="uint8")
# xanh = (0, 255, 0)
# cv2.line(khung, (0,0), (300,300), xanh)
# #cv2.imshow("Anh", khung)

# do = (0, 0, 255)
# cv2.line(khung, (300,0), (0,300), do, 20)
# #cv2.imshow("Anh", khung)

# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # cv2.rectangle(khung, (10, 10), (60, 60), xanh)
# # cv2.imshow("Anh", khung)
# # cv2.waitKey(0)

# cv2.rectangle(khung, (50, 200), (200, 225), do, 5)
# cv2.imshow("Anh", khung)
# cv2.waitKey(0)

# xanhduong = (255, 0, 0)
# cv2.rectangle(khung, (200, 50), (225, 125), xanhduong, -1)
# cv2.imshow("Anh", khung)
# cv2.waitKey(0)

#màu trắng
# trang = (255, 255, 255)

# for r in range(0, 175, 25):
#     cv2.circle(khung, (khung.shape[1] // 2, khung.shape[0] // 2), r, trang)

# cv2.imshow("Anh", khung)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)  
# #pts = pts.reshape((-1,1,2))
# cv2.polylines(khung, [pts], True, (0,255,255), 3)
# cv2.imshow("Anh", khung)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # org
# org = (00, 185)
  
# # fontScale
# fontScale = 1
   
# # Red color in BGR
# color = (0, 0, 255)
  
# # Line thickness of 2 px
# thickness = 2
   
# # Using cv2.putText() method
# image = cv2.putText(image, "OpenCV", org, cv2.FONT_HERSHEY_SIMPLEX, fontScale, 
#                  color, thickness, cv2.LINE_AA, False)
  
# # # Using cv2.putText() method
# # image = cv2.putText(image, "OpenCV", org, cv2.FONT_HERSHEY_SIMPLEX, fontScale,
# #                   color, thickness, cv2.LINE_AA, True) 
  
# # Displaying the image
# cv2.imshow("Ảnh phản chiếu", image) 
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imshow('Picture 1', image)
# cv2.waitKey()
# cv2.destroyAllWindows()

# img = cv2.imread("sample.png")
# img1 = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
# # ghép ảnh theo chiều ngang
# img2 = np.hstack((img, img1))
# cv2.imshow("GaussianBlur", img2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()