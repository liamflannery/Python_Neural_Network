class HiddenLayer:
    def __init__(self, size) -> None:
        self.size = size
    
    def get_size(self):
        print(self.size)




hidden_layer_count = 5
hidden_layer_size = 2

hidden_layers = [HiddenLayer(hidden_layer_size) for x in range(0,hidden_layer_count)]

for layer in hidden_layers:
    layer.get_size()




