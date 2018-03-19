from PIL import Image
import numpy as np
import math

tileSize = 13 #defines the square size of a given tile

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
        self.dimensions = [] #x,y dimensions of the photo
        
    def getDimensions(self):
        self.dimensions.append(len(self.photo[0])) #x
        self.dimensions.append(len(self.photo)) #y
        print(self.dimensions)

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
    #print(grid.dimensions[1]//tileSize, grid.dimensions[0]//tileSize)
    for y in range(0, len(grid.photo)//tileSize):
        grid.squares.append([]) #makes a new level in 2D array
        for x in range(0, len(grid.photo[0])//tileSize):
            for a in range(0,tileSize):
                for b in range(0,tileSize):
                    squareNum += grid.photo[y*tileSize + a][x*tileSize + b]
                    
            grid.squares[y].append(int(squareNum//(tileSize*tileSize)))
            squareNum = 0
    #print(grid.squares)
            
def numPyIfy(img): #creates a 2D array of pixels
    img = np.asarray(img, dtype=np.float32)
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
    print(len(grid.photo), len(grid.photo[0]))
    makeSquares(grid)
    print(grid.squares)
    
    
main()
