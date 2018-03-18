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
        
    def makeSquares(self):
        

def numPyIfy(img):
    instance.image = np.asarray(instance.image, dtype=np.float32)

def makeSquares

def resizeImage (img, xyDims): 
    for instanceType in instances:
        for instance in instanceType:
            instance.image = instance.image.resize(size, Image.ANTIALIAS)

def main():
    imageName = "monaLisa.jpg"
    image = Image.open(imageName).convert('BW') #image must be in same folder
    storedImg = image.copy()
    image.close()
    grid = Grid()
    grid.photo = storedImg
    
main()
