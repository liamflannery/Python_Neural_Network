import math


class Node: #inputNodes(Node, nodeOutputValue) # inputWeights(Node, weightValue)
    
    
    def __init__(self, inputNodes, inputWeights, input, layerType, biasValue):
        self.inputNodes = ""
        self.inputWeights = ""
        self.biasValue = ""
        self.outputValue = ""
        self.layerType = layerType
        
        if(layerType == 0):
            self.outputValue = input
        
        else:
            self.inputNodes = inputNodes
            self.inputWeights = inputWeights
            self.biasValue = biasValue
            self.outputValue = self.computeValue()
            
            
    
        
    def computeValue(self):
        returnValue = self.biasValue
        for x in range(len(self.inputNodes)):
            weight = self.inputWeights[x]
            node = self.inputNodes[x]
            returnValue += node.getOutputValue() * weight
        
        if self.layerType == 2:
            return returnValue
        else:
            return self.ActivationFunction(returnValue)
    
    def ActivationFunction(self, value):
        # return value
        return 1 / (1 + math.exp(-value))
    
    def getOutputValue(self):
        return self.outputValue
    
    def toString(self):
        nodeString = "\nNODE \n"
        if(self.inputNodes != ""):
            nodeString += "Input Values: " 
            for node in self.inputNodes:
                nodeString += str(node.getOutputValue()) + " "
            nodeString += "\n"
        if(self.inputWeights != ""):
            nodeString += "Weights: " + str(self.inputWeights) + "\n"
        if(self.biasValue != ""):
            nodeString += "Bias: " + str(self.biasValue) + "\n"
        if(self.outputValue != ""):
            nodeString += "Output Value: " + str(self.outputValue) + "\n"
            

        return nodeString
        
    
        

    
        
    