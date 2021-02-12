class Perceptron():
    def __init__(self, weights: [float], bias: float):
        self.bias = bias
        self.weights = weights

    def activation(self):
        """
        Een Dictionary list met alle binaire mogelijkheden wordt gemaakt en ieder wordt met de gate weights opgetelt en
        gekeken of de bias het positief of negatief maakt. E.G: (1,0) + OR (weight = 0.5 & bias = 0.5) = 1. Wat het resultaat opslaat in de
        dictionary van de binaire mogelijkheid E.G: {(1,0): 1}
        :return: Een list met voor alle mogelijkheden de output dat ook in een list zit
        """
        allposibleinputs = []
        for x in range(0, 2 ** len(self.weights)):
            allposibleinputs.append(tuple([int(i) for i in list(bin(x)[2:].zfill(len(self.weights)))]))
        # maakt een list met alle binaire mogelijkheden
        possibilityOutputList = {i : [] for i in allposibleinputs} # maakt een dictionary aan die alle mogelijke inputs hen resultaat bijhoudt
        for possibility in range(len(allposibleinputs)): #loopt door index van de mogelijkheden E.G: [[1,1]] -> [1,1]
            totalsum = 0
            for index in range(len(allposibleinputs[possibility])): #loopt door de index van 1 mogelijkheid E.G.: [1,1] -> 1 -> 1
                totalsum += allposibleinputs[possibility][index] * self.weights[index] #waarbij elk antwoord toegevoegd wordt aan een totaal antwoord variabele
            output = totalsum - self.bias #de som in een variabele gedaan
            if output >= 0:#en te checken of dit positief is
                possibilityOutputList[allposibleinputs[possibility]].append(1) #deze uitkomst komt dan in de value van de key van de mogelijkheid
            else:
                possibilityOutputList[allposibleinputs[possibility]].append(0)
        return possibilityOutputList

    def gateUnderstander(self, usedGate, amountofinputs):
        """
        Wordt aangeroepen om een String GateNaam om te zetten in een Perceptron met de getelde aantal inputs als gewichten
        :param usedGate: De onwetende string gate
        :param amountofinputs: hoeveel inputs er voor deze gate zijn
        :return: een perceptron class die de weights en bias insteld voor de gevonden gate
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


'''DE PRINT VOOR DE STANDAARD GATES'''
print('\nInvert Port')
INVERT_port = Perceptron(weights=[-1], bias=0)
print(INVERT_port.activation())

print('\nAND Port')
AND_port = Perceptron(weights=[0.5, 0.5], bias=1)
print(AND_port.activation())

print('\nOR Port')
OR_port = Perceptron(weights=[0.5, 0.5], bias=0.5)
print(OR_port.activation())


print('\nNor Port')
NOR_port = Perceptron(weights=[-0.5, -0.5], bias=0)
print(NOR_port.activation())

print('\nParty Port')
Party_port = Perceptron(weights=[0.6, 0.3, 0.2], bias=0.4)
print(Party_port.activation())


