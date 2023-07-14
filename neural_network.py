import Layer as LayerClass

Layer = LayerClass.Layer

def Network(
    i1, i2,
    weights,
    biasValues,
    trainingValues
):
    
    hiddenLayerWeights = dict()
    hiddenLayerWeights[0] = [weights[0], weights[3]]
    hiddenLayerWeights[1] = [weights[1],weights[4]]
    hiddenLayerWeights[2] = [weights[3],weights[5]]

    outputLayerWeights = dict()
    outputLayerWeights[0] = [weights[6],weights[8],weights[10]]
    outputLayerWeights[1] = [weights[7],weights[9],weights[11]]
    
    


    inputLayer = Layer([i1,i2], None, None, biasValues, 0)
    hiddenLayer = Layer(inputLayer, hiddenLayerWeights, 3, biasValues[0:3], 1)
    outputLayer = Layer(hiddenLayer, outputLayerWeights, 2, biasValues[3:5], 2)

    
    # print(
    #     "Input Layer:", inputLayer.toString(),"\n"
    #     "Hidden Layer: ", hiddenLayer.toString(),"\n"
    #     "Output Layer: ", outputLayer.toString()
    # )
    if trainingValues == None:
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

