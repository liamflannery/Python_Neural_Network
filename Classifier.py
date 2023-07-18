import random
import neural_network as NetworkClass
Network = NetworkClass.Network
## change classes to lower snake case
def classify(    
    i1, i2,
    weights,
    biases
    ):

    output = Network(
            i1, i2,
            weights, biases, None
    )
    output_1 = round(output()[0], 2)
    output_2 = round(output()[1], 2)
    
    # return [output_1, output_2]
    # print(output_1, output_2)
    return 0 if output_1 > output_2 else 1

def node_cost(output, expectedOutput):
    error = output - expectedOutput
    return error * error

def cost(weights, biases, training_red, training_blue):
    cost = 0
    for index, row in training_red.iterrows():
        cost += node_cost(classify(row["x_variable"], row["y_variable"], weights, biases), 1)
    for index, row in training_blue.iterrows():
        cost += node_cost(classify(row["x_variable"], row["y_variable"], weights, biases), 0)
    return cost



# def get_random_weight():
#     return random.randint(-10,10) / 10.0

# def get_random_bias():
#     return random.randint(-100,100)

# initialWeights = []
# initialBiases = []
# for x in range(0,12):
#     initialWeights.append(get_random_weight())
# for x in range(0,5):
#     initialBiases.append(get_random_bias())



def classify_points(
            weights,
            biases,
            training_red, training_blue, graphResolution
                   ):
    
    red_x_values = []
    red_y_values = []
    blue_x_values = []
    blue_y_values = []
    costValue = cost(weights=weights, biases=biases, training_red=training_red, training_blue=training_blue)
    for x in range(0, graphResolution * 100):
        for y in range(0, graphResolution * 100):
            if classify(
                x/graphResolution, y/graphResolution,
                weights,
                biases
            ) == 1:
                red_x_values.append(x/graphResolution)
                red_y_values.append(y/graphResolution)
                
            else:
                blue_x_values.append(x/graphResolution)
                blue_y_values.append(y/graphResolution)
               
    
    return [red_x_values, red_y_values, blue_x_values, blue_y_values, costValue]

# for w1 in [z * 0.1 for z in range(-10, 10)]:
#     for w2 in [z * 0.1 for z in range(-10, 10)]:
#         for w3 in [z * 0.1 for z in range(-10, 10)]:
#             for w4 in [z * 0.1 for z in range(-10, 10)]:
#                 for b1 in range(-100, 100):
#                     for b2 in range(-100, 100):
#                         for b3 in range(-100, 100):
#                             redVals = []
#                             blueVals = []
#                             for x in range(-100, 100):
#                                 for y in range(-100, 100):
#                                     if Classify(
#                                         x, y,
#                                         w1, 1, 1,
#                                         w2, 1, 1,
#                                         w3, w4,
#                                         1, 1,
#                                         1, 1,
#                                         b1,b2,b3,0,0
#                                     ) > 0:
#                                         blueVals.append([x,y])
#                                     else:
#                                         redVals.append([x,y])
                            
#                             # if ((len(redVals) != 0 and len(blueVals) != 0)):
#                             print(w1, w2, w3, w4, "\n")
#                             print("RED VALS: ", len(redVals) , " \n" , "BLUE VALS: " , len(blueVals))
            
        
        
