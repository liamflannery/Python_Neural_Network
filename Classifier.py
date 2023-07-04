import neural_network as NetworkClass
Network = NetworkClass.Network

def Classify(    
    i1, i2,
    hw11, hw12, hw13,
    hw21, hw22, hw23,
    ow11, ow12,
    ow21, ow22,
    ow31, ow32
    ):

    output = Network(
            i1, i2,
            hw11, hw12, hw13,
            hw21, hw22, hw23,
            ow11, ow12,
            ow21, ow22,
            ow31, ow32
    )
    output_1 = round(output()[0], 2)
    output_2 = round(output()[1], 2)
        
    return 0 if output_1 > output_2 else 1


def ClassifyPoints(
            hw11, hw12, hw13,
            hw21, hw22, hw23,
            ow11, ow12,
            ow21, ow22,
            ow31, ow32
                   ):
    
    red_x_values = []
    red_y_values = []
    blue_x_values = []
    blue_y_values = []
    
    for x in range(0, 100):
        for y in range(0, 100):
            if Classify(
                x, y,
                hw11, hw12, hw13,
                hw21, hw22, hw23,
                ow11, ow12,
                ow21, ow22,
                ow31, ow32
            ) == 1:
                red_x_values.append(x)
                red_y_values.append(y)
                
            else:
                blue_x_values.append(x)
                blue_y_values.append(y)
               
 
    return [red_x_values, red_y_values, blue_x_values, blue_y_values]