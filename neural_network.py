from Layer import InputLayer, HiddenLayer, OutputLayer

InputLayer = InputLayer.InputLayer
HiddenLayer = HiddenLayer.HiddenLayer
OutputLayer = OutputLayer.OutputLayer

class NeuralNetwork:
    
    weights = dict()
    def __init__(self, input_layer_size, hidden_layer_size, hidden_layer_count, output_layer_size):
       self.input_layer = InputLayer(input_layer_size)
       self.hidden_layers = [HiddenLayer(hidden_layer_size) for x in range(0,hidden_layer_count)]
       self.output_layer = OutputLayer(output_layer_size)
       
       self.hidden_layers[0].set_feed_in_layer(self.input_layer)
       for x in range(1,hidden_layer_count):
           self.hidden_layers[x].set_feed_in_layer(self.hidden_layers[x-1])
       self.output_layer.set_feed_in_layer(self.hidden_layers[hidden_layer_count - 1])

       self.initialise_weights()
    
    
    def initialise_weights(self):
        self.weights.update(self.input_layer.initialise_weights())
        for layer in self.hidden_layers: self.weights.update(layer.initialise_weights())
        self.weights.update(self.output_layer.initialise_weights())
    
    def print_neural_network(self):
        self.input_layer.print_layer_size()
        for layer in self.hidden_layers: layer.print_layer_size()
        self.output_layer.print_layer_size() 
        print(len(self.weights))


   


nn = NeuralNetwork(2, 2, 1, 2)
nn.print_neural_network()