import cv2

if __name__ == '__main__' :
    # Read imagePNG Overlay and Image Rotation using OpenCV | CVZone

    img = cv2.imread("1.jpg")
    cv2.namedWindow("Image",2)
    r = cv2.selectROI("Image", img)

    ## Display the roi
    
    if r is not None:
        x,y,w,h = r
        
        cropped_image = img[int(r[1]):int(r[3]+r[1]),
                        int(r[0]):int(r[2]+r[0])]
        print(cropped_image.shape)
        cv2.imwrite("now.png", cropped_image)
        pt1 = (r[0], r[1])
        pt2 = (r[2]+r[0], r[3]+r[1])
        colors = (0,255,0)
        
        rect_img = cv2.rectangle(img, pt1, pt2, colors)
        cv2.namedWindow("Finalusing opencv Image",2)
        cv2.imshow("Final",rect_img)

    cv2.waitKey(0)