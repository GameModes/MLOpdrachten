import PerceptronLayer as pL


class PerceptronNetwork:
    layers = None
    structure = None
    def __init__(self, amountofinput, structure):
        pass

        # for layer in structure:  # loop door alle layers uit de structures
        #     layers.append(pL.PerceptronLayer(layer[0], layer[1]))

            # print(layer)

    def get_layers(self, amountofinput, structure):
        pass
        # layers = []
        # layers.append(pL.PerceptronLayer(structure[0][0], structure[0][1]))
        # return layers

    # def feed_forward(self, inputs):
    #     allposibleinputs = self.give_correct_possibilities(inputs)
    #     for input in allposibleinputs:
    #         print(input)
    def __str__(self):
        return str(self.layers)

    # def give_correct_possibilities(self, inputs):
    #     possible_inputs1 = [[0], [1]]
    #     possible_inputs2 = [[0, 0],[1, 0], [0, 1], [1, 1]]
    #     possible_inputs3 = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [1, 1, 0], [0, 0, 1], [1, 0, 1], [0, 1, 1], [1, 1, 1]]
    #     if inputs == 1:
    #         allposibleinputs = possible_inputs1
    #     elif inputs == 2:
    #         allposibleinputs = possible_inputs2
    #     else:
    #         allposibleinputs = possible_inputs3
    #     return allposibleinputs

# print('\nXOR Port')
#                                  layer 1                   layer 2
#                           1 & 2de poort | input amounts  1ste poort | input amount
XOR = PerceptronNetwork(2, [ [ ["OR", "NAND"], [2, 2] ], [ ["AND"], [2] ] ])
print(XOR.get_layers(2, [ [ ["OR", "NAND"], [2, 2] ], [ ["AND"], [2] ] ]))

# XOR.feed_forward(2)
# XOR.network[1].layer[0].set_bias(weights=[[-0.5], [1.5])
# XOR.network[1].layer[1].set_bias(weights=[-1.5])
# XOR.network[1].layer[0].set_weights(weights=[[1, 1], [-1, -1])
# XOR.network[1].layer[1].set_weights(weights=[1, 1])

# print(XOR.activation([0, 0])) #0
# print(XOR.activation([0, 1])) #1
# print(XOR.activation([1, 0])) #1
# print(XOR.activation([1, 1])) #0


# print('\nHalf Adder Port')
# Half_Adder_Port = PerceptronNetwork([0.5, 0.5], 1, [0.5, 0.5], 1, [0.5, 0.5], 1, [0.5, 0.5], 1, [0.5, 0.5], 0, 1)
# print(Half_Adder_Port.activation([0, 0])) #0, 0
# print(Half_Adder_Port.activation([0, 1])) #0, 1
# print(Half_Adder_Port.activation([1, 0])) #0, 1
# print(Half_Adder_Port.activation([1, 1])) #1, 0
