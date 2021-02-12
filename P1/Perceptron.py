class Perceptron():
    def __init__(self, weights: [float], bias: float):
        self.bias = bias
        self.weights = weights

    def give_correct_possibilities(self):
        possible_inputs1 = [(0), (1)]
        possible_inputs2 = [(0, 0), (1, 0), (0, 1), (1, 1)]
        possible_inputs3 = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (0, 0, 1), (1, 0, 1), (0, 1, 1), (1, 1, 1)]
        if len(self.weights)  == 1:
            allposibleinputs = possible_inputs1
        elif len(self.weights) == 2:
            allposibleinputs = possible_inputs2
        else:
            allposibleinputs = possible_inputs3
        return allposibleinputs

    def activation(self):
        allposibleinputs = self.give_correct_possibilities()
        # Voeg de activatiefunctie toe om uitvoer (output) te leveren bij een gegeven invoer (input).
        possibilityOutputList = {i : None for i in allposibleinputs} #put all posibilities in a dictionary to save the output
        for possibility in range(len(allposibleinputs)):
            totalsum = 0
            # print(possibility)
            # print(allposibleinputs)
            try:
                for index in range(len(allposibleinputs[possibility])): #dit is mijn manier om de perceptron uit te rekenen
                    totalsum += allposibleinputs[possibility][index] * self.weights[index] #waarbij de totaal antwoord elk antwoord toegevoegd wordt
            except TypeError:
                totalsum += possibility * self.weights[0]
            output = totalsum - self.bias #de som in een variabele gedaan
            if output >= 0:#en te checken of dit positief is
                possibilityOutputList[allposibleinputs[possibility]] = 1
                # possibilityOutputList.append(1)
            else:
                possibilityOutputList[allposibleinputs[possibility]] =0
                # possibilityOutputList.append(0)
        return possibilityOutputList

    def gateUnderstander(self, usedGate, amountofinputs):
        savedGates = {
            "INVERT": Perceptron(weights=[-1], bias=0),
            "AND": Perceptron(weights=[1 for inputamount in range(amountofinputs)], bias=amountofinputs*1),
            "OR": Perceptron(weights=[0.5 for inputamount in range(amountofinputs)], bias=0.5),
            "NOR": Perceptron(weights=[-1 for inputamount in range(amountofinputs)], bias=0),
            "NAND": Perceptron(weights=[-1 for inputamount in range(amountofinputs)], bias=amountofinputs*-1.5)}
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
        return self.weights, self.bias


# print('\nAND Port')
# AND_port = Perceptron(weights=[0.5, 0.5], bias=1)
# print(AND_port.activation())
#
# print('\nInvert Port')
# INVERT_port = Perceptron(weights=[-1], bias=0)
# print(INVERT_port.activation())
#
# #
# print('\nAND Port')
# AND_port = Perceptron(weights=[0.5, 0.5], bias=1)
# print(AND_port.activation())
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


