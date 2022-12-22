import numpy as np
import pyautogui as rbt
from PIL import Image
import os, cv2
from matplotlib import pyplot as plt


def get_screenshot(saveName, folder_path=os.getcwd()):
    file_path = os.path.join(folder_path, saveName)
    rbt.screenshot().save(file_path)


def find_matches(fp_crp, fp_ss):
    # open Images
    im_ss = Image.open(fp_ss)
    im_crp = Image.open(fp_crp)
    
    arr_ss = np.asarray(im_ss)     # convert img to arrays
    arr_crp = np.asarray(im_crp)   # convert img to arrays

    y_ss, x_ss = arr_ss.shape[:2]       # get img pixel dimension
    y_crp, x_crp = arr_crp.shape[:2]    # get img pixel dimension

    #print(x_ss, y_ss)

    
    xstop = x_ss - x_crp + 1
    ystop = y_ss - y_crp + 1

    matches = []

    
    for xmin in range(0, xstop):
        for ymin in range(0, ystop):
            xmax = xmin + x_crp
            ymax = ymin + y_crp

            arr_test_img = arr_ss[ymin:ymax, xmin:xmax]     # Extract subimage
            arr_test = (arr_test_img == arr_crp)            # Create test matrix
            #print(arr_test)
            if arr_test.all():                              # Only consider exact matches
                matches.append([xmin, ymin,     # origin point of crop img on screenshot
                                int(xmin+0.5*x_crp), # mid point on crop img x axis
                                int(ymin+0.5*y_crp)  # mid point on crop img y axis
                                ]
                                )

    return matches


def LocImgOnScreen(fp_img):
    fp_ss = "screenshot.PNG"
    get_screenshot(fp_ss)
    img_loc = find_matches(fp_img, fp_ss)[0]
    img_mid_point_loc = [img_loc[2], img_loc[3]]
    return img_mid_point_loc


def SaveImgOnScreen(cord, img_name, folder_path=os.getcwd()):
    crop_cord = (cord[0], cord[1], cord[2]-cord[0], cord[3]-cord[1])
    file_path = os.path.join(folder_path, img_name+".PNG")
    rbt.screenshot(region=crop_cord).save(file_path)
    
    
def LocAllImgOnScreen(templateImgPath):
    FolderPath = os.path.dirname(templateImgPath)       # get working dir
    ss_name = "screenshot.PNG"                          # screenshot filename
    get_screenshot(ss_name, folder_path=FolderPath)     # take and save ss
    
    img_rgb = cv2.imread(os.path.join(FolderPath, ss_name))  # load screenshot
    img_gry = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)     # convert to gray

    
    template = cv2.imread(templateImgPath, 0)   # load template image    
    w, h = template.shape[::-1]                 # get template image size

    # perform matching between screenshot and template images
    res = cv2.matchTemplate(img_gry, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    #print(loc)
    loc_cord = [(int(pt[0]+(w*0.5)), int(pt[1]+(h*0.5))) for pt in zip(*loc[::-1])]
    #for pt in zip(*loc[::-1]):
    #   cv2.rectangle(img_rgb, pt, (pt[0]+w, pt[1]+h), (0,0,255), 2)
    #   loc_cord.append(int(pt[0]+(w*0.5)), int(pt[1]+(h*0.5)))
    #cv2.imwrite("res.png", img_rgb)
    return loc_cord

    

def CaptureImageOnScreen(imgName, imgSaveFolderPath=os.getcwd(), cords=0):
    imgFilePath = os.path.join(imgSaveFolderPath, imgName + ".PNG")

    if cords:
        cord = [cords[0], cords[1], cords[2], cords[3]] # x1, y1, x2, y2
    else:
        pos1=input("position Mouse point for Pos1 and press Enter: ")
        pos1 = rbt.position()
        print("\n*** Point Captured ***"); print()
        pos2=input("position Mouse point for Pos2 and press Enter: ")
        pos2 = rbt.position()
        print("\n*** Point Captured ***")
        cord = [pos1[0], pos1[1], pos2[0], pos2[1]]
    crop_cord = (cord[0], cord[1], cord[2]-cord[0], cord[3]-cord[1])
    rbt.screenshot(region=crop_cord).save(imgFilePath)
    print("\n*** Image Captured and saved successfully ***")

    
    



    
if __name__ == "__main__":
    imgFolderPath = r"C:\Users\q38226\Documents\Python\hla\img"
    templateImg = os.path.join(imgFolderPath, "smt_exec_run_status_img.PNG")
    print(LocAllImgOnScreen(templateImg))


    
