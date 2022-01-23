import numpy as np
import cv2


def WeightedMedianFilter(img,Wgt):

    xWgtShape = Wgt.shape[0]
    yWgtShape = Wgt.shape[1]
    xImgShape = img.shape[0]
    yImgShape = img.shape[1]

    rayXWgtShape = (int)(xWgtShape-1)/2
    rayYWgtShape = (int)(yWgtShape-1)/2

    xWMF = xImgShape
    yWMF = yImgShape

    weightedMedianFilter = np.zeros((xWMF, yWMF))

    i = 0
    while (i < xImgShape):
        j = 0
        while(j < yImgShape):
            target_Img = img[i,j]
            if (i<rayXWgtShape or j<rayYWgtShape or i >= (xImgShape - rayXWgtShape) or j >= (yImgShape-rayYWgtShape)):
                weightedMedianFilter[i,j] = img[i,j]
            else :
                m = 0
                weightedMedian = 0
                weightedSum = 0
                while (m<xWgtShape):
                    n = 0
                    while (n<yWgtShape):
                        target_Wgt = Wgt[m,n]
                        weightedSum += target_Wgt
                        coef_i = (int)(i-rayXWgtShape+m)
                        coef_j = (int)(j-rayYWgtShape+n)
                        weightedMedian += target_Wgt*img[coef_i, coef_j]
                        n+=1
                    m+=1
                #weightedMedianFilter[i,j] = weightedMedian / weightedSum
                weightedMedianFilter[i,j] = weightedMedian
            j+=1
        i+=1
    
    return weightedMedianFilter

def WeightedMedianFilter_Pass(img,Wgt):
    pass

def GetCLAHE(i):
    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(i)
    #cv.imwrite('clahe_2.jpg',cl1)
    return cl1

def WeightedMedianFilterV2(img,Wgt):

    xWgtShape = Wgt.shape[0]
    yWgtShape = Wgt.shape[1]
    xImgShape = img.shape[0]
    yImgShape = img.shape[1]

    rayXWgtShape = (int)(xWgtShape-1)/2
    rayYWgtShape = (int)(yWgtShape-1)/2

    xWMF = xImgShape
    yWMF = yImgShape

    weightedMedianFilter = np.zeros((xWMF, yWMF))

    i = 0
    while (i < xImgShape):
        j = 0
        while(j < yImgShape):
            target_Img = img[i,j]
            if (i<rayXWgtShape or j<rayYWgtShape or i >= (xImgShape - rayXWgtShape) or j >= (yImgShape-rayYWgtShape)):
                weightedMedianFilter[i,j] = img[i,j]
            else :
                m = 0
                weightedMedian = 0
                weightedSum = 0
                while (m<xWgtShape):
                    n = 0
                    while (n<yWgtShape):
                        target_Wgt = Wgt[m,n]
                        weightedSum += target_Wgt
                        coef_i = (int)(i-rayXWgtShape+m)
                        coef_j = (int)(j-rayYWgtShape+n)
                        weightedMedian += target_Wgt*img[coef_i, coef_j]
                        n+=1
                    m+=1
                weightedMedianFilter[i,j] = weightedMedian / weightedSum
                #weightedMedianFilter[i,j] = weightedMedian
            j+=1
        i+=1
    
    return weightedMedianFilter