import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import shutil

def RecreateMasks_train():  
    
    source = "Data/imc4solo/train/"
    target = "Data/Train/labels/"
    
    for i in range(0,10):
        I = mpimg.imread(source + "00" + str(i) + "_masks.png")
        mpimg.imsave(target + "00" + str(i) + ".png",I)
    for i in range(10,100):
        I = mpimg.imread(source + "0" + str(i) + "_masks.png")
        mpimg.imsave(target + "0" + str(i) + ".png",I)
    for i in range(100,1000):
        I = mpimg.imread(source + str(i) + "_masks.png")
        mpimg.imsave(target + str(i) + ".png",I)

def RecreateMasks_test():  
    
    source = "Data/imc4solo/test/"
    target = "Data/Test/labels/"
    
    for i in range(0,10):
        I = mpimg.imread(source + "00" + str(i) + "_masks.png")
        mpimg.imsave(target + "00" + str(i) + ".png",I)
    for i in range(10,40):
        I = mpimg.imread(source + "0" + str(i) + "_masks.png")
        mpimg.imsave(target + "0" + str(i) + ".png",I)

        
def Copy_RenamePics_Train():
    
    source = "Data/imc4solo/train/"
    target = "Data/Train/shapes_train/"
    for i in range(0,10):
        shutil.copy(source + "00" + str(i) + "_img.png", target + "00" + str(i) + ".png") #shutil.copy(source, target)
    for i in range(10,100):
        shutil.copy(source + "0" + str(i) + "_img.png", target + "0" + str(i) + ".png") 
    for i in range(100,1000):
        shutil.copy(source + str(i) + "_img.png", target + str(i) + ".png")   
        

def Copy_RenamePics_Test():
    
    source = "Data/imc4solo/test/"
    target = "Data/Test/shapes_test/"
    for i in range(0,10):
        shutil.copy(source + "00" + str(i) + "_img.png", target + "00" + str(i) + ".png") #shutil.copy(source, target)
    for i in range(10,40):
        shutil.copy(source + "0" + str(i) + "_img.png", target + "0" + str(i) + ".png") 
    
if __name__ == "__main__":
    
    os.system("mkdir -p Data/Train/shapes_train/ Data/Train/labels/ Data/Train/annotations/")
    Copy_RenamePics_Train()
    os.system("mkdir -p Data/Test/shapes_test/ Data/Test/labels/ Data/Test/annotations/")
    Copy_RenamePics_Test()
    RecreateMasks_train()
    RecreateMasks_test()
