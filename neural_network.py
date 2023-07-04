import Layer as LayerClass

Layer = LayerClass.Layer


hiddenLayerWeights = dict()
hiddenLayerWeights[0] = [1,0]
hiddenLayerWeights[1] = [0,0]
hiddenLayerWeights[2] = [0,0]

outputLayerWeights = dict()
outputLayerWeights[0] = [1,0,0]
outputLayerWeights[1] = [0,0,0]


inputLayer = Layer([1,1], None, None)
hiddenLayer = Layer(inputLayer, hiddenLayerWeights, 3)
outputLayer = Layer(hiddenLayer, outputLayerWeights, 2)

outputLayer.toString()





# inputLayer = list()
# inputLayer.append(Node(None, None, 2))
# inputLayer.append(Node(None, None, 1))

# hiddenLayer = list()

# inputToHiddenWeights = dict()

# for node in inputLayer:
#     inputToHiddenWeights[node] = 1
    
# hiddenLayer.append(Node(inputLayer, inputToHiddenWeights.copy(), None))
# hiddenLayer.append(Node(inputLayer, inputToHiddenWeights.copy(), None))
# hiddenLayer.append(Node(inputLayer, inputToHiddenWeights.copy(), None))

# outputLayer = list()
# hiddenToOutputWeights = dict()

# for node in hiddenLayer:
#     hiddenToOutputWeights[node] = 1
    

# outputLayer.append(Node(hiddenLayer, hiddenToOutputWeights.copy(), None))
# outputLayer.append(Node(hiddenLayer, hiddenToOutputWeights.copy(), None))


# for node in outputLayer:
#     print(node.outputValue)

