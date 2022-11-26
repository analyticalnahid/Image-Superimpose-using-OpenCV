# importing library
import cv2
from rembg import remove
from PIL import Image


def cropImage(): 
    
    #read image
    image = cv2.imread('2.jpg', cv2.IMREAD_UNCHANGED)
    cv2.namedWindow("Image",2)
    
    #select ROI.
    roi = cv2.selectROI("Image", image)
    
    #crop image
    cropped_image = image[int(roi[1]):int(roi[3]+roi[1]),
                        int(roi[0]):int(roi[2]+roi[0])]
    
    #pass the croped image 
    input = cropped_image
    
    #path of saved image
    output_path = 'Backremoval.png'
    
    #remove background
    output = remove(input)
    
    #saved image
    cv2.imwrite(output_path, output)
    
    #create outline 
    rmBackImg = cv2.imread('Backremoval.png')
    img_gray = cv2.cvtColor(rmBackImg, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 3, 4, cv2.THRESH_BINARY)
    contours4, hierarchy4 = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    image_copy = rmBackImg.copy()
    cv2.drawContours(image_copy, contours4, -1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imwrite("outline.png", image_copy)
    
    
    #transparent image
    file_name1 = "outline.png"
    src1 = cv2.imread(file_name1, 1)
    tmp1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
    _,alpha1 = cv2.threshold(tmp1,0,255,cv2.THRESH_BINARY)
    b, g, r = cv2.split(src1)
    rgba1 = [b,g,r, alpha1]
    dst1 = cv2.merge(rgba1,4)
    cv2.imwrite("transparent.png", dst1)
    
    #convert jpg to png
    cv2.imwrite("2.png", image)
 
    #open image
    background = Image.open("2.png")
    foreground = Image.open("transparent.png")
    
    #get x and y coordinate
    y1 = roi[1]
    x1 = roi[0]

    #paster image
    background.paste(foreground, (x1, y1), foreground)
    background.show()
    

    cv2.waitKey(0)
    
    
    cv2.destroyAllWindows()


cropImage()

