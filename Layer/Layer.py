import Node as NodeClass

Node = NodeClass.Node

class Layer:
    weights = dict()
    feed_in_layer = None
    def __init__(self, layerSize):
        self.nodes = [Node() for x in range(0,layerSize)]
    
    def print_layer_size(self):
        print(len(self.nodes))

    def get_nodes(self):
        return self.nodes
    
    def initialise_weights(self):
        if(self.feed_in_layer):
            for input_node in self.feed_in_layer.get_nodes():
                for node in self.nodes:
                    self.weights[(input_node, node)] = 0
                    node.set_weight((input_node, node), 0)

        return self.weights
        
        
    
    def set_feed_in_layer(self, layer):
        self.feed_in_layer = layer