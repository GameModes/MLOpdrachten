import PerceptronLayer as pL


class PerceptronNetwork:
    layers = None
    structure = None
    def __init__(self, amountInput, structure):
        struct = []
        for layer in structure:
            struct.append(pL.PerceptronLayer(layer[0], layer[1]))
        self.structure = struct
        self.amountInput = amountInput

    def feed_forward(self):
        """
        :return een dictionary "full_network_structure" die bijhoudt wat er gebeurt bij elke mogelijkheid
        """
        full_network_structure = self.structure[0].listsOfGatesinLayer #de eerste layer wordt gebruikt als template
        for ind in range(len(self.structure)):
            # print("\nnetwork: " + str(full_network_structure))
            try:
                currentlayer = self.structure[ind]
                nextlayer = self.structure[ind+1]
                currentLayerValues = list(currentlayer.listsOfGatesinLayer.values())
                # print("current:" + str(currentlayer.listsOfGatesinLayer))
                # print("next: " + str(nextlayer.listsOfGatesinLayer))
                for current_Key, current_Value in full_network_structure.items():
                    #source: https://stackoverflow.com/questions/17793364/python-iterate-dictionary-by-index
                    for next_Key, next_Value in nextlayer.listsOfGatesinLayer.items():
                        if next_Key == tuple(current_Value): #om de output als input voor de ander te gebruiken, moet de type verandert worden naar tuple
                            full_network_structure[current_Key] = next_Value
            except IndexError:
                continue
        return full_network_structure

    def combi_gates(self, Gate1, Gate2):
        print(Gate1)
        print(Gate2)
        # for current_Key, current_Value in Gate1:
        pass

    def __str__(self):
        return str(self.layers)

def get_combi_gates(Gate1, Gate2):
    combiGate = Gate2
    for Key, Value in Gate1.items():
        combiGate[Key].append(Gate1.get(Key)[0])
    return combiGate


print('\nXOR Port')
#                                  layer 1                   layer 2
#                           1 & 2de poort | input amounts  1ste poort | input amount
# XOR = PerceptronNetwork(2, [ [ ["OR", "NAND"], [2, 2] ], [ ["AND", "AND"], [2, 2] ], [ ["NOR"], [2] ] ])
XOR = PerceptronNetwork(2, [ [ ["OR", "NAND"], [2, 2] ], [ ["AND"], [2] ] ])
print("Network Structure: " + str(XOR.feed_forward()))


print('\nHalf Adder Port')
Half_Adder_Port = PerceptronNetwork(2, [ [ ["AND"], [2] ] ])
Gate1 = XOR.feed_forward()
Gate2 = Half_Adder_Port.feed_forward()
print("Network Structure: " + str(get_combi_gates(Gate1, Gate2)))