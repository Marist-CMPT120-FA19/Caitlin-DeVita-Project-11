#Caitlin De Vita
#caitin.devita1@marist.edu
#Sphere Class Assignment

import math

class Sphere:

    def __init__(self , radius):
        self.radius = radius
        self.surfaceArea = (4) * (math.pi) * (self.radius ** 2)
        self.volume = (4/3) * (math.pi) * (self.radius ** 3)
    #Creates a sphere having the given radius.
        
    def getRadius(self):
        return self.radius
    #Returns the radius of the sphere.
        
    def getsurfaceArea(self):
        return self.surfaceArea
    #Returns the surface area of the sphere.
        
    def getvolume(self):
        return self.volume
    #Returns the volume of the sphere.
    
        
def main():
    
    radius = float(input("What is the raduis of the sphere?"))
    theSphere = Sphere(radius)
    print("The volume of sphere is" , theSphere.getvolume())
    print("The surface area of sphere is" , theSphere.getsurfaceArea())
   
    
if __name__ == '__main__':
    main()
