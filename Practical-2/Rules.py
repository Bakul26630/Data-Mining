# Define these rules in a separate text file and read them.
# Species should be one of the following values: setosa, versicolor or virginica.
# All measured numerical properties of an iris should be positive.
# The petal length of an iris is at least 2 times its petal width.
# The sepal length of an iris cannot exceed 30 cm.
# The sepals of an iris are longer than its petals.
def isFloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

class Iris:
    def __init__(self,sepalLength,sepalWidth,petalLength,petalWidth,species) -> None:
        self.sepalLength = float(sepalLength) if isFloat(sepalLength) else 0.0
        self.sepalWidth = float(sepalWidth) if isFloat(sepalWidth) else 0.0
        self.petalLength = float(petalLength) if isFloat(petalLength) else 0.0
        self.petalWidth = float(petalWidth) if isFloat(petalWidth) else 0.0
        self.species=species
    
    def checkSpecies(self):
        possibleValue = ["setosa","versicolor","virginica"]
        if (self.species in possibleValue):
            return True
        return False
    
    def checkPetalLengthSign(self):
        if (self.petalLength>0.0):
            return True
        return False
    
    def checkPetalWidthSign(self):
        if(self.petalWidth>0.0):
            return True
        return False
    def checkSepalLengthSign(self):
        if(self.sepalLength>0.0):
            return True
        return False
    def checkSepalWidthSign(self):
        if(self.sepalWidth>0.0):
            return True
        return False
    
    def checkPetalLength(self):
        if(self.petalLength>=2*self.petalWidth):
            return True
        else:
            return False

    def checkSepalLength(self):
        if(self.sepalLength>0 and self.sepalLength<=30):
            return True
        return False

    def compareSepalPetal(self):
        if(self.sepalLength>self.petalLength):
            return True
        return False