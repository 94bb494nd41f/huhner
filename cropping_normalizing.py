import cv2
import os


path = "cropping/"
liste = os.listdir(path)
path_cropping = "cropping/cropped+normalized/"
### define cropping window
y1 = 1000
y2 = 1944
x1 = 750
x2 = 2000

for i in liste:
    if ".jpg" in i:
        img_load = cv2.imread(path + i)
        img_cropped = img_load[y1:y2, x1:x2]

        gray_image = cv2.cvtColor(img_cropped, cv2.COLOR_BGR2GRAY)
        mean = cv2.mean(gray_image)[0]
        print(i, mean)
        if mean >= 22:
            gray_norm = cv2.normalize(gray_image, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
            cv2.imwrite((path_cropping + i), gray_norm)