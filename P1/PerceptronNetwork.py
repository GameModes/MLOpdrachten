import PerceptronLayer as pL
'''
Guy heeft me geholpen met het structuur geven, omdat we beide hetzelfde plan hadden om StandaardGates te gebruiken in het network systeem
'''


class PerceptronNetwork:
    layers = None
    structure = None

    def __init__(self, amountInput, structure):
        """
        zet het hele structuur in een simpelere en overzichtelijker struct list variabele
        :param amountInput: Het begin input dat wordt gebruikt
        :param structure: het hele structuur (nested list) met gates en hun inputs
        """
        struct = []
        for layer in structure:
            struct.append(pL.PerceptronLayer(layer[0], layer[1]))
        self.structure = struct
        self.amountInput = amountInput

    def feed_forward(self):
        """
        dmv een full_network_structure/current dictionary en nextlayer dictionary wordt er bij de current dictionary telkens geupdate
        met waardes van de nextlayer dictionary:
        e.g:
        ["OR", "NAND"] geeft
        {(0, 0): [0,1]*, (0, 1): [1,1]*, (1, 0): [1,1]*, (1, 1)*: [1,0]*}
        +         |                |               |                |
        AND geeft:v                v               v                v
        {(0, 0): [0], *(0, 1):   [1], *(1, 0):   [1], *(1, 1):   [0]}

        :return een dictionary "full_network_structure" die bijhoudt wat er gebeurt bij elke mogelijkheid
        """
        full_network_structure = self.structure[0].listsOfGatesinLayer  # de eerste/current layer wordt gebruikt als template
        for ind in range(len(self.structure)):
            try:
                nextlayer = self.structure[ind + 1]
                for current_Key, current_Value in full_network_structure.items():
                    # source: #https://realpython.com/iterate-through-dictionary-python/
                    for next_Key, next_Value in nextlayer.listsOfGatesinLayer.items():
                        if next_Key == tuple(
                                current_Value):  # om de output als input voor de ander te gebruiken, moet de type verandert worden naar tuple
                            full_network_structure[current_Key] = next_Value
            except IndexError: #omdat het telkens vergelijkt met de volgende layer, moet er een try except in komen om het te stoppen voordat het errored
                continue
        return full_network_structure

def get_combi_gates(Gate1, Gate2):
    """
    bij het gebruik van nieuwere gates kan er gebruikt gemaakt worden om eerdere gemaakt gates met elkaar te combineren
    E.G.: om een Half adder te krijgen heb je een XOR en een AND nodig dus die wordt gebruik in de prints onder de functies
    {(0, 0): [0], (0, 1): [1], (1, 0): [1], (1, 1): [0]}
    {(0, 0): [0], (0, 1): [0], (1, 0): [0], (1, 1): [1]}
    ----------------------------------------------------- +
    {(0, 0): [0, 0], (0, 1): [0, 1], (1, 0): [0, 1], (1, 1): [1, 0]}
    :param Gate1: de eerste gate wat een dictionary is, die alle inputs en outputs al bevat
    :param Gate2: de tweede gate wat een dictionary is, die alle inputs en outputs al bevat
    :return:
    """
    combiGate = Gate2
    for Key, Value in Gate1.items(): #https://realpython.com/iterate-through-dictionary-python/
        combiGate[Key].append(Gate1.get(Key)[0])
    return combiGate

'''DE PRINT OM DE GEAVANCEERDE GATES TE GEBRUIKEN'''
#PRINT CONCEPT:
#                                  layer 1                  |            layer 2
#                           1ste & 2de poort | input amount | 1ste & 2de poort | input amount
# XOR = PerceptronNetwork(2, [ [ ["OR", "NAND"], [2, 2] ],     [ ["AND", "AND"], [2, 2] ])

print('\nXOR Port')
XOR = PerceptronNetwork(2, [[["OR", "NAND"], [2, 2]], [["AND"], [2]]])
print("Network Structure: {0}".format(XOR.feed_forward()))

print('\nHalf Adder Port')
Half_Adder_Port = PerceptronNetwork(2, [[["AND"], [2]]])
print("Network Structure: {0}".format(get_combi_gates(XOR.feed_forward(), Half_Adder_Port.feed_forward())))
