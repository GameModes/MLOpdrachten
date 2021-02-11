import PerceptronLayer as pl

class PerceptronNetwork:

    def __init__(self, amountofinput, structure):
        gate
        for layer in structure:
            for gateInteraction in layer:
                gate = gateInteraction[0]
                bias = gateInteraction[1]
                print(gate)
                print(bias)

    # def feed_forward(self, inputs):



# print('\nXOR Port')
#                            layer 1             layer 2
#                         1ste poort  2de poort   1ste poort
XOR = PerceptronNetwork(2, [[["OR"], ["NAND"]], [["AND"]]])
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
