class Perceptron():
    def __init__(self, weights: [float], bias: float):
        self.bi = bias
        self.wgt = weights

    def activation(self, input: [int]):
        # Voeg de activatiefunctie toe om uitvoer (output) te leveren bij een gegeven invoer (input).
        totalsum = 0
        for index in range(len(input)): #dit is mijn manier om de perceptron uit te rekenen
            totalsum += input[index] * self.wgt[index] #waarbij de totaal antwoord elk antwoord toegevoegd wordt
        output = totalsum - self.bi #de som in een variabele gedaan
        if output >= 0:#en te checken of dit positief is
            return 1
        else:
            return 0

    def gateUnderstander(self, usedGate):
        savedGates = {
            "INVERT": Perceptron(weights=[-1], bias=0),
            "AND": Perceptron(weights=[0.5, 0.5], bias=1),
            "OR": Perceptron(weights=[0.5, 0.5], bias=0.5),
            "NOR": Perceptron(weights=[-0.5, -0.5], bias=0),
            "NAND": Perceptron(weights=[-1, -1], bias=0)}
        return savedGates[usedGate]

    def get_weights(self):
        return self.weights

    def set_weights(self, weights):
        self.weights = weights

    def get_bias(self):
        return self.bias

    def set_bias(self, bias):
        self.bias = bias

    def __str__(self):
        # string om de weights en bias te printen
        return self.wgt, self.bi


# print('\nInvert Port')
# INVERT_port = Perceptron(weights=[-1], bias=0)
# print(INVERT_port.activation([0]))
# print(INVERT_port.activation([1]))
#
# print('\nAND Port')
# AND_port = Perceptron(weights=[0.5, 0.5], bias=1)
# print(AND_port.activation([0, 0]))
# print(AND_port.activation([0, 1]))
# print(AND_port.activation([1, 0]))
# print(AND_port.activation([1, 1]))
#
#
# print('\nOR Port')
# OR_port = Perceptron(weights=[0.5, 0.5], bias=0.5)
# print(OR_port.activation([0, 0]))
# print(OR_port.activation([0, 1]))
# print(OR_port.activation([1, 0]))
# print(OR_port.activation([1, 1]))
#
#
# print('\nNor Port')
# NOR_port = Perceptron(weights=[-0.5, -0.5], bias=0)
# print(NOR_port.activation([0, 0]))
# print(NOR_port.activation([0, 1]))
# print(NOR_port.activation([1, 0]))
# print(NOR_port.activation([1, 1]))
#
#
# print('\nParty Port')
# Party_port = Perceptron(weights=[0.6, 0.3, 0.2], bias=0.4)
# print(Party_port.activation([0, 0, 0]))
# print(Party_port.activation([0, 1, 0]))
# print(Party_port.activation([1, 0, 0]))
# print(Party_port.activation([1, 1, 0]))
# print(Party_port.activation([0, 0, 1]))
# print(Party_port.activation([0, 1, 1]))
# print(Party_port.activation([1, 0, 1]))
# print(Party_port.activation([1, 1, 1]))


