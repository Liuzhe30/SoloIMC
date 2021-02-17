import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import shutil

def RecreateMasks_train():  
    
    source = "Data/CellPose_Data/Train/"
    target = "Data/Train/labels/"
    
    for i in range(0,10):
        I = mpimg.imread(source + "00" + str(i) + "_masks.png")
        mpimg.imsave(target + str(i + 1) + ".png",I)
    for i in range(10,100):
        I = mpimg.imread(source + "0" + str(i) + "_masks.png")
        mpimg.imsave(target + str(i + 1) + ".png",I)
    for i in range(100,540):
        I = mpimg.imread(source + str(i) + "_masks.png")
        mpimg.imsave(target + str(i + 1) + ".png",I)
    #
    #mpimg.imsave('D:/imc/SoloCell/train/labels/004_masks.png',I)
    
    #color = []
    #for i in img:
        #for j in i:
            #if(j not in color):
                #color.append(j)
    #print(color)
    #color.sort()
    #print(color)
    #print(len(color))
    
    #print(type(img))
    #io.imshow(img)
    #io.show()    


def RecreateMasks_test():  
    
    source = "Data/CellPose_Data/Test/"
    target = "Data/Test/labels/"
    
    for i in range(0,10):
        I = mpimg.imread(source + "00" + str(i) + "_masks.png")
        mpimg.imsave(target + str(i + 1) + ".png",I)
    for i in range(10,68):
        I = mpimg.imread(source + "0" + str(i) + "_masks.png")
        mpimg.imsave(target + str(i + 1) + ".png",I)

        
def Copy_RenamePics_Train():
    
    source = "Data/CellPose_Data/Train/"
    target = "Data/Train/shapes_train/"
    for i in range(0,10):
        shutil.copy(source + "00" + str(i) + "_img.png", target + str(i + 1) + ".png") #shutil.copy(source, target)
    for i in range(10,100):
        shutil.copy(source + "0" + str(i) + "_img.png", target + str(i + 1) + ".png") 
    for i in range(100,540):
        shutil.copy(source + str(i) + "_img.png", target + str(i + 1) + ".png")   
        

def Copy_RenamePics_Test():
    
    source = "Data/CellPose_Data/Test/"
    target = "Data/Test/shapes_test/"
    for i in range(0,10):
        shutil.copy(source + "00" + str(i) + "_img.png", target + str(i + 1) + ".png") #shutil.copy(source, target)
    for i in range(10,68):
        shutil.copy(source + "0" + str(i) + "_img.png", target + str(i + 1) + ".png") 
    
if __name__ == "__main__":
    
    #Copy_RenamePics_Train()
    #Copy_RenamePics_Test()
    #RecreateMasks_train()
    #RecreateMasks_test()
