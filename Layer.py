import Node as NodeClass

Node = NodeClass.Node

class Layer:
    def __init__(self, inputLayer, layerWeights, layerSize):
        self.nodeList = []
        if(layerWeights):
            for x in range(layerSize):
                self.nodeList.append(Node(inputLayer.getNodes(), layerWeights[x], None, False))
        else:
            for x in range(len(inputLayer)):
                self.nodeList.append(Node(None, None, inputLayer[x], True))
    
    def getNodes(self):
        return self.nodeList
    
    def getValues(self):
        nodes = list()
        for node in self.nodeList:
            nodes.append(node.outputValue)
        return nodes