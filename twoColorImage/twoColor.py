from PIL import Image
import numpy as np
import math

class Square:
    def __init__(self):
        self.c = None #0 if White, 1 if Black. Determines direction of slider
        self.avgColor = None #the average pixel color of the square
        
        #Keep track of the square dimensions & location on the Map
        #
        #top left
        self.x = None
        self.y = None
        #
        #top right
        self.xEnd = None
        self.yEnd = None
        
        #Neighbors (to know where the slider goes)
        self.N = None
        self.E = None
        self.S = None
        self.W = None
        
class Grid:
    def __init__(self):
        self.squares = [] #2D array of all squares on the grid in l-r u-d order
        self.photo = None
        

def makeSquares(imgArray):
    return None    

def resizeImage (img, xyDims): 
    for instanceType in instances:
        for instance in instanceType:
            instance.image = instance.image.resize(size, Image.ANTIALIAS)
            
def numPyIfy(img): #creates a 2D array of pixels
    img = np.asarray(img, dtype=np.float32)
    return img
            
def makeImage(imageName):
    img = Image.open(imageName).convert('L') #image must be in same folder
    storedImg = img.copy()
    img.close()
    storedImg = numPyIfy(storedImg)
    return storedImg

def main():
    img = makeImage("monaLisa.jpg")
    grid = Grid()
    grid.photo = img
    print(grid.photo)
    grid.squares = makeSquares(grid.photo)
    
main()
