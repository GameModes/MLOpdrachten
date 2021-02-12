import Perceptron as per

class PerceptronLayer:
    layer = None
    def __init__(self, gatesInLayer, listOfAmountOfInputs): #vraagt op de gatesindelayer en welk naam ze hebben (misschien moet ik de layer nummer er bij zetten)
        listsOfGatesinLayer = []
        layer = []
        p = per.Perceptron(weights=[], bias=0) #default
        for gate in range(len(gatesInLayer)): #
            if gatesInLayer[gate] in ["INVERT", "AND", "OR", "NOR", "NAND"]: #checkt of het wel een goede gate is
                layer.append(p.gateUnderstander(gatesInLayer[gate], listOfAmountOfInputs[gate])) #zet het in een list genaamd layer
            else: #anders stop alles en zeg dat het niet goed is
                print("Gate or Entire Input wrongly typed")
                break
        for x in range(len(layer)):
            try:
                listsOfGatesinLayer.append(layer[x].activation())
            except IndexError:
                listsOfGatesinLayer.append(layer[x].activation())

        self.listsOfGatesinLayer = listsOfGatesinLayer
        self.layer = layer

    def __str__(self):
        return str(self.listsOfGatesinLayer) #waarschijnlijk wilde ik hier ene list terug geven van alle gates, maar dat is niet goed gegaan

pl = PerceptronLayer(["NAND", "OR", "INVERT"], [2, 2, 1])
print(pl)


# print(pl.layer[0].activation([1,1]))