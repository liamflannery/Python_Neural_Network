import Layer as LayerClass

Layer = LayerClass.Layer

def Network(
    i1, i2,
    hw11, hw12, hw13,
    hw21, hw22, hw23,
    ow11, ow12,
    ow21, ow22,
    ow31, ow32,
    b1,b2,b3,b4,b5
):
    
    hiddenLayerWeights = dict()
    hiddenLayerWeights[0] = [hw11,hw21]
    hiddenLayerWeights[1] = [hw12,hw22]
    hiddenLayerWeights[2] = [hw13,hw23]

    outputLayerWeights = dict()
    outputLayerWeights[0] = [ow11,ow21,ow31]
    outputLayerWeights[1] = [ow12,ow22,ow32]
    
    biasValues = [b1,b2,b3,b4,b5]


    inputLayer = Layer([i1,i2], None, None, biasValues, 0)
    hiddenLayer = Layer(inputLayer, hiddenLayerWeights, 3, biasValues[0:3], 1)
    outputLayer = Layer(hiddenLayer, outputLayerWeights, 2, biasValues[3:5], 2)

    
    # print(
    #     "Input Layer:", inputLayer.toString(),"\n"
    #     "Hidden Layer: ", hiddenLayer.toString(),"\n"
    #     "Output Layer: ", outputLayer.toString()
    # )
    
    return outputLayer.getValues






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

