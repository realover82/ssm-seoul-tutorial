import cv2
import motor_end
from tensorflow.keras.models import load_model
import numpy as np

camera = cv2.VideoCapture(0)
camera.set(3,640)
camera.set(4,480)
model = load_model("/home/pi/autonomousCar/AIcar/deep_auto (1).h5")


# i = 0
# carstate = "stop"
# file_path = "/home/pi/autonomousCar/AIcar/data/"

while camera.isOpened():
    # key = cv2.waitKey(1)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    
    # elif key == 81:
    #     print("left")
    #     carstate = "left"
    #     motor_end.motor_one_speed(30)
    #     motor_end.motor_two_speed(0)
        
    # elif key == 82:
    #     print("go")
    #     carstate = "go"
    #     motor_end.motor_one_speed(30)
    #     motor_end.motor_two_speed(30)
    # elif key == 83:
    #     print("right")
    #     carstate = "right"
    #     motor_end.motor_one_speed(0)
    #     motor_end.motor_two_speed(30)
    # elif key == 84:
    #     print("back")
    #     carstate = "stop"
    #     motor_end.motor_one_speed(0)
    #     motor_end.motor_two_speed(0)
        
    _, image = camera.read()
    image = cv2.flip(image, -1)
    # cv2.imshow('main', image)
    
    height, _, _ = image.shape
    save_image = image[int(height/3*2): , :, :]
    save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2YUV)
    save_image = cv2.GaussianBlur(save_image, (3,3), 0)
    save_image = cv2.resize(save_image, (200,66))
    #cv2.imshow('yuv', save_image)
    # cv2.imshow('main', save_image)
    x = np.asarray([save_image])
    predict = np.argmax(model.predict(x))
    
    #  if carstate == "left":
    if predict == 0:
        motor_end.motor_one_speed(20)
        motor_end.motor_one_speed(20)
        # print("L")
        # cv2.imwrite("%s_%05d_%s.png" % (file_path, i, "L"),save_image)
        # i +=1
    # elif carstate == "right":
    elif predict == 1:
        motor_end.motor_one_speed(20)
        motor_end.motor_one_speed(0)
        # print("R")
        # cv2.imwrite("%s_%05d_%s.png" % (file_path, i, "R"),save_image)
        # i +=1
    # elif carstate == "go":
    elif predict == 2:
        motor_end.motor_one_speed(0)
        motor_end.motor_one_speed(20)
        # print("G")
        # cv2.imwrite("%s_%05d_%s.png" % (file_path, i, "G"),save_image)
        # i +=1
        
    # if carstate == "left":
    #     print("L")
    #     cv2.imwrite("%s_%05d_%s.png" % (file_path, i, "L"),save_image)
    #     i +=1
    # elif carstate == "right":
    #     print("R")
    #     cv2.imwrite("%s_%05d_%s.png" % (file_path, i, "R"),save_image)
    #     i +=1
    # elif carstate == "go":
    #     print("G")
    #     cv2.imwrite("%s_%05d_%s.png" % (file_path, i, "G"),save_image)
    #     i +=1
        
# cv2.distroyAllwindows()

    