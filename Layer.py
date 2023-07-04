import Node as NodeClass

Node = NodeClass.Node

class Layer:
    def __init__(self, inputLayer, layerWeights, layerSize):
        self.nodeList = []
        if(layerWeights):
            for x in range(layerSize):
                self.nodeList.append(Node(inputLayer.getNodes(), layerWeights[x], None))
        else:
            for x in range(len(inputLayer)):
                self.nodeList.append(Node(None, None, inputLayer[x]))
    
    def getNodes(self):
        return self.nodeList
    
    def toString(self):
        for node in self.nodeList:
            print(node.outputValue)