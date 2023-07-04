class Node: #inputNodes(Node, nodeOutputValue) # inputWeights(Node, weightValue)
    
    
    def __init__(self, inputNodes, inputWeights, input):
        if(input):
            self.outputValue = input
        
        else:
            self.inputNodes = inputNodes
            self.inputWeights = inputWeights
            self.outputValue = self.computeValue()
    
        
    def computeValue(self):
        returnValue = 0
        for x in range(len(self.inputNodes)):
            weight = self.inputWeights[x]
            node = self.inputNodes[x]
            returnValue += node.outputValue * weight
        return returnValue
    
    def outputValue(self):
        return self.outputValue
    