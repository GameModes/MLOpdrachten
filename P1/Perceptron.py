class Perceptron():
    def __init__(self, weights: [float], bias: float):
        self.bias = bias
        self.weights = weights

    def activation(self):
        """

        - Zet alle mogelijkheden in een dictionary met als value een lege list die ingevuld kan worden
        - Loopt door inputs en tel bij elke mogelijke input de totale gewicht van de inputs
        - Dan wordt gecheckt of het met de bias positief is, zo ja dan is het een 1 als output en wordt het
        in de lege list van de dictionary toegevoegd
        :return: Een list met voor alle mogelijkheden de output dat ook in een list zit
        """
        from itertools import product
        allposibleinputs = [i for i in product(range(2), repeat=len(self.weights))] #- Vraagt alle mogelijkheden voor inputs in een list
        # Voeg de activatiefunctie toe om uitvoer (output) te leveren bij een gegeven invoer (input).
        possibilityOutputList = {i : [] for i in allposibleinputs} #put all posibilities in a dictionary to save the output
        for possibility in range(len(allposibleinputs)):
            totalsum = 0
            for index in range(len(allposibleinputs[possibility])):
                totalsum += allposibleinputs[possibility][index] * self.weights[index] #waarbij de totaal antwoord elk antwoord toegevoegd wordt
            output = totalsum - self.bias #de som in een variabele gedaan
            if output >= 0:#en te checken of dit positief is
                possibilityOutputList[allposibleinputs[possibility]].append(1)
            else:
                possibilityOutputList[allposibleinputs[possibility]].append(0)
        return possibilityOutputList

    def gateUnderstander(self, usedGate, amountofinputs):
        """
        Wordt aangeroepen om een String GateNaam om te zetten in een Perceptron met de getelde aantal inputs als gewichten
        :param usedGate:
        :param amountofinputs:
        :return:
        """
        savedGates = {
            "INVERT": Perceptron(weights=[-1], bias=0),
            "AND": Perceptron(weights=[1 for inputamount in range(amountofinputs)], bias=amountofinputs*1),
            "OR": Perceptron(weights=[0.5 for inputamount in range(amountofinputs)], bias=0.5),
            "NOR": Perceptron(weights=[-1 for inputamount in range(amountofinputs)], bias=0),
            "NAND": Perceptron(weights=[-1.5 for inputamount in range(amountofinputs)], bias=amountofinputs*-1)}
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
# #
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


