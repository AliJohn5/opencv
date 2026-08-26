import cv2 as cv
import numpy as np

def create_black_img(h=300,w=400):
    return np.zeros((h,w,3) , dtype=np.uint8)

def create_white_img(h=300,w=400):
    img = np.zeros((h,w,3) , dtype=np.uint8)
    img[:] = 255
    return img

def create_gradient_img(h=300,w=400):
    img = np.zeros((h,w,3) , dtype=np.uint8)

    for i in range(h):
        img[i,:] = [200 - (i//2), 100 , 50 + (i // 2)]

    return img

def translate_img(img, dx, dy):
    '''
         1 0 dx
         0 1 dy
    '''
    translating_matrix = np.float32([[1, 0, dx] , [0, 1, dy]])
    h, w, c = img.shape
    new_img = cv.warpAffine(img,translating_matrix,(w, h))
    return new_img

def rotate_img(img, cx, cy, ang, scale = 1.0):
    ratation_matrix = cv.getRotationMatrix2D((cx,cy),ang,scale)
    h, w, c = img.shape
    new_img = cv.warpAffine(img,ratation_matrix,(w, h))
    return new_img

def resize_scale(img,scale_w,scale_h):
    return cv.resize(img,(0,0),fx=scale_w,fy=scale_h,interpolation=cv.INTER_AREA)

def resize_to(img,new_w,new_h):
    return cv.resize(img,(new_w,new_h),interpolation=cv.INTER_AREA)

def create_img_with_shapes1():
    canva  = create_white_img()

    cv.rectangle(img=canva,pt1=(10,10),pt2=(110,110),color=(255,0,0),thickness=-1)

    cv.rectangle(img=canva,pt1=(150,10),pt2=(300,110),color=(255,0,255),thickness=5)

    return canva


def create_img_with_shapes2():
    canva  = create_white_img()

    cv.circle(img=canva,center=(200,200),radius=50,color=(0,255,255),thickness=5)

    cv.line(img=canva,color=(255,255,0),pt1=(0,200),pt2=(400,200),thickness=5,)

    cv.putText(
        img=canva,
        text="Hello World",
        org=(20,280),
        color=(10,10,10),
        fontScale=0.7,
        thickness=6,
        lineType=cv.LINE_AA,
        fontFace=cv.FONT_HERSHEY_SIMPLEX
    )

    return canva


def merge_two_images(img1, img2):
    img1_temp = img1.copy()
    img2_temp = img2.copy()

    w, h , c = img1.shape
    for i in range(h):
        for j in range(w):
            #print(img1_temp[j,i])
            if(
                img1_temp[j,i,0] == 255 
              and  img1_temp[j,i,1] == 255
              and img1_temp[j,i,2] == 255):
                img1_temp[j,i] = [0,0,0]

    w, h , c = img2.shape
    for i in range(h):
        for j in range(w):
            if(
                img2_temp[j,i,0] == 255 
              and  img2_temp[j,i,1] == 255
              and img2_temp[j,i,2] == 255):
                img2_temp[j,i] = [0,0,0]

    new_img = cv.add(img1_temp,img2_temp)
    w, h , c = new_img.shape
    for i in range(h):
        for j in range(w):
            if(
                new_img[j,i,0] == 0 
              and  new_img[j,i,1] == 0
              and new_img[j,i,2] == 0):
                new_img[j,i] = [255,255,255]

    return new_img

def create_my_logo():
    canva  = create_white_img()
    
    cv.circle(img=canva,center=(200,150),radius=50,color=(255,255,0),thickness=-1)

    return canva
    
def change_bg():
    logo = create_my_logo()
    bg = create_gradient_img()
    cv.imshow("logo", logo)
    cv.imshow("bg", bg)

    h ,w , c = logo.shape

    mask  = np.zeros((h,w),dtype=np.uint8)
    cv.circle(img=mask,center=(200,150),radius=50,color=255,thickness=-1)
    cv.imshow("mask", mask)

    mask_inv = cv.bitwise_not(mask)
    cv.imshow("mask_inv", mask_inv)

    mask_fg = cv.bitwise_and(logo,logo,mask=mask)
    cv.imshow("mask_fg", mask_fg)

    mask_bg = cv.bitwise_and(bg,bg,mask=mask_inv)
    cv.imshow("mask_bg", mask_bg)

    new_img = cv.add(mask_bg,mask_fg)
    cv.imshow("new_img", new_img)
    
    return

def change_brightness_and_contarst():
    img = create_gradient_img()
    cv.imshow("img", img)

    brightness_img = cv.add(img,np.array([70.0,70.0,70.0]))
    cv.imshow("brightness_img", brightness_img)

    ## img * alpha + beta
    contarst = cv.convertScaleAbs(img,alpha=1.5,beta=40.0)
    cv.imshow("contarst", contarst)

    return

def main():
    print("starting code")
    change_brightness_and_contarst()
    cv.waitKey(0)


if __name__ == "__main__":
    main()