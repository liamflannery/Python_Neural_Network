import neural_network as NetworkClass
Network = NetworkClass.Network

def Classify(    
    i1, i2,
    hw11, hw12, hw13,
    hw21, hw22, hw23,
    ow11, ow12,
    ow21, ow22,
    ow31, ow32,
    b1,b2,b3,b4,b5
    ):

    output = Network(
            i1, i2,
            hw11, hw12, hw13,
            hw21, hw22, hw23,
            ow11, ow12,
            ow21, ow22,
            ow31, ow32,
            b1,b2,b3,b4,b5
    )
    output_1 = round(output()[0], 2)
    output_2 = round(output()[1], 2)
    
    # return [output_1, output_2]
    # print(output_1, output_2)
    return 0 if output_1 > output_2 else 1


def Cost():
    return 0

def ClassifyPoints(
            hw11, hw12, hw13,
            hw21, hw22, hw23,
            ow11, ow12,
            ow21, ow22,
            ow31, ow32,
            b1,b2,b3,b4,b5,
            training_red, training_blue
                   ):
    
    red_x_values = []
    red_y_values = []
    blue_x_values = []
    blue_y_values = []
    cost = Cost(training_red, training_blue)
    for x in range(0, 100):
        for y in range(0, 100):
            if Classify(
                x, y,
                hw11, hw12, hw13,
                hw21, hw22, hw23,
                ow11, ow12,
                ow21, ow22,
                ow31, ow32,
                b1,b2,b3,b4,b5
            ) == 1:
                red_x_values.append(x)
                red_y_values.append(y)
                
            else:
                blue_x_values.append(x)
                blue_y_values.append(y)
               
 
    return [red_x_values, red_y_values, blue_x_values, blue_y_values, cost]




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
            
        
        
