import os
from PIL import Image
import shutil

originPath = "./images/origin/"

preIdCard = 'id'
preBankCard = 'bankCard'
preCarID = 'car'
preDriveLicence = 'drive'
preInvoice = 'invo'
preEstate = 'estate'
preBusinessID = 'buzi'
preCommonText = 'txt'

prefixes = [
    preIdCard, preBankCard, preCarID, preDriveLicence, preInvoice, preEstate, preBusinessID, preCommonText
]

def resize_by_size(maxSize,srcPath,desPath): 
    maxSize *= 1024  
    im = Image.open(srcPath)  
    size_tmp = os.path.getsize(srcPath)  
    q = 100  
    while size_tmp > maxSize and q > 0:  
        out = im.resize(im.size, Image.ANTIALIAS)  
        print "saving image to desPath: "+ desPath
        out.save(desPath, quality=q)  
        size_tmp = os.path.getsize(desPath)  
        q -= 5  
    if q == 100:  
        shutil.copy(srcPath, desPath)  

def files_in_dir(dirPath):
    for root, dirs, files in os.walk(dirPath):
        # print "Current root is "+ root + " files are: "+ " ".join(files)
        # print 'dirs = ' + "".join(dirs)
        return files


if __name__=='__main__':  
    Quanlity = 500
    desQuanlityPath = "images/"+str(Quanlity)
    for dirName in prefixes:
        dirPath = originPath+dirName
        containImages = files_in_dir(dirPath)
        for i in range(len(containImages)):
            imgName = containImages[i]
            if not imgName.lower().endswith("jpg"):
                continue
            imgPath = os.path.join(dirPath, imgName)
            print "now processing image from " + imgPath
            desDirName = os.path.join(desQuanlityPath,dirName)

            if not os.path.exists(desDirName):
                os.makedirs(desDirName)

            desImgPath = os.path.join(desDirName, imgName)

            if os.path.exists(desImgPath):
                os.remove(desImgPath)

            resize_by_size(Quanlity,imgPath,desImgPath)

            

        

