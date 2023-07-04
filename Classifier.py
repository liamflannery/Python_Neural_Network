

def Classify(input_1, input_2, weight_1_1, weight_2_1, weight_1_2, weight_2_2, bias_1, bias_2):
    output_1 = input_1 * weight_1_1 + input_2 * weight_2_1 + bias_1
    output_2 = input_1 * weight_1_2 + input_2 * weight_2_2 + bias_2
    
    output_1 = round(output_1, 2)
    output_2 = round(output_2, 2)
        
    return 0 if output_1 > output_2 else 1


def ClassifyPoints(weight_1_1, weight_2_1, weight_1_2, weight_2_2, bias_1, bias_2):
    
    red_x_values = []
    red_y_values = []
    blue_x_values = []
    blue_y_values = []
    
    for x in range(0, 100):
        for y in range(0, 100):
            if Classify(x, y, weight_1_1, weight_2_1, weight_1_2, weight_2_2, bias_1, bias_2) == 1:
                red_x_values.append(x)
                red_y_values.append(y)
                
            else:
                blue_x_values.append(x)
                blue_y_values.append(y)
               
 
    return [red_x_values, red_y_values, blue_x_values, blue_y_values]