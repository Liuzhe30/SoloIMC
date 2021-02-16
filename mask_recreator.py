import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

I = mpimg.imread("D:/imc/data/cellpose/train/004_masks.png")
mpimg.imsave('D:/imc/SoloCell/train/labels/004_masks.png',I)

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