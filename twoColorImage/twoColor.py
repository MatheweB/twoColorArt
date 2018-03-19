from PIL import Image
import numpy as np
import math
from scipy.misc import toimage #IMAGE PLOTTER

tileSize = 30 #defines the square size of a given tile

class Square:
    def __init__(self, c, avgColor, x, y):
        self.c = c #0 if White, 1 if Black. Determines direction of slider
        self.avgColor = avgColor #the average pixel color of the square
        
        #Keep track of the square dimensions & location on the Map
        #
        #top left
        self.x = x
        self.y = x
        #
        #bottom right
        self.xEnd = x + tileSize
        self.yEnd = y + tileSize
        
        #Neighbors (to know where the slider goes)
        self.N = None
        self.E = None
        self.S = None
        self.W = None

    def getNeighbors(self, squares, gridIndex):
        return None
        
class Grid:
    def __init__(self):
        self.squares = [] #2D array of all squares on the grid in l-r u-d order
        self.photo = None #2D array also
        self.pixelPhoto = [] #Lower-res 2D array

    def showPixelPhoto(self):
        toimage(self.pixelPhoto).show()

def makeDimensionsWork(img):
    x = img.size[0]
    y = img.size[1]
    
    while x%tileSize != 0:
        x += 1
    while y%tileSize != 0: 
        y += 1
        
    img = img.resize([x,y], Image.ANTIALIAS)
    return img
    

def makeSquares(grid):
    squareNum = 0
    totalSquares = 0
    
    for y in range(0, len(grid.photo)//tileSize):
        grid.squares.append([]) #makes a new level in 2D array
        grid.pixelPhoto.append([])
        for x in range(0, len(grid.photo[0])//tileSize):
            for a in range(0,tileSize):
                for b in range(0,tileSize):
                    squareNum += grid.photo[y*tileSize + a][x*tileSize + b]
            
            totalSquares += 1
            newSquare = Square(totalSquares%2, int(squareNum//(tileSize*tileSize)), x*tileSize, y*tileSize)
            grid.squares[y].append(newSquare)
            grid.pixelPhoto[y].append(int(squareNum//(tileSize*tileSize)))
            squareNum = 0
            
def numPyIfy(img): #creates a 2D array of pixels
    img = np.asarray(img)
    return img
            
def makeImage(imageName):
    img = Image.open(imageName).convert('L') #Black & White
    storedImg = img.copy()
    img.close()

    storedImg = makeDimensionsWork(storedImg)
    storedImg = numPyIfy(storedImg)

    return storedImg

def main():
    grid = Grid()
    grid.photo = makeImage("monaLisa.jpg")
    makeSquares(grid)
    grid.showPixelPhoto()
    
    
main()
