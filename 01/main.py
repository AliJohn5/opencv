import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("sample.jpeg")

if img is None:
    raise FileNotFoundError("please check the path")

## unresizeable window
cv.imshow("sample",img)

## resizeable window
#cv.namedWindow("win1",cv.WINDOW_NORMAL)
#cv.imshow("win1",img)
#cv.waitKey(0)


## image shape
height, width, channels = img.shape
print(f"Image Shape:\nheight: {height}, width: {width}, channels: {channels}")

## crop the img
crpoed_img = img[0:3, 0:3 , :]
print("croped_img: ",crpoed_img)

## crop the img and show it
crpoed_img2 = img[0:100 , 0:300, :]
cv.imshow("croped_img2", crpoed_img2)

print(img.shape, crpoed_img2.shape)
cv.waitKey(0)
cv.destroyAllWindows()


rgb_img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
gray_img = cv.cvtColor(rgb_img,cv.COLOR_BGR2GRAY)

fig, axis = plt.subplots(1, 3, figsize=(12, 5))

axis[0].imshow(img)
axis[0].set_title("BGR image")
axis[0].axis("off")

axis[1].imshow(rgb_img)
axis[1].set_title("RGB image")
axis[1].axis("off")

axis[2].imshow(gray_img, cmap="gray")
axis[2].set_title("Gray image")
axis[2].axis("off")

cv.imshow("gray img", gray_img)

plt.tight_layout()
plt.show()





