import Node as NodeClass

Node = NodeClass.Node

class Layer:
    def __init__(self, inputLayer, layerWeights, layerSize, biasValues, layerType):
        self.nodeList = []
        if(layerType > 0):
            for x in range(layerSize):
                self.nodeList.append(Node(inputLayer.getNodes(), layerWeights[x], None, layerType, biasValues[x]))
        else:
            for x in range(len(inputLayer)):
                self.nodeList.append(Node(None, None, inputLayer[x], layerType, biasValues[x]))
    
    def getNodes(self):
        return self.nodeList
    
    def getValues(self):
        nodes = list()
        for node in self.nodeList:
            nodes.append(node.getOutputValue())
        return nodes
    
    def toString(self):
        nodeString = ""
        
        for node in self.nodeList:
            nodeString += node.toString()
        return nodeString