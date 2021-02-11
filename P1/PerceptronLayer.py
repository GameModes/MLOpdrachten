import Perceptron as per

class PerceptronLayer:
    def __init__(self, gatesInLayer, gateNames): #vraagt op de gatesindelayer en welk naam ze hebben (misschien moet ik de layer nummer er bij zetten)
        self.layer = None
        layer = []
        p = per.Perceptron(weights=[], bias=0) #default
        for gate in gatesInLayer[0]: #
            if gate in ["INVERT", "AND", "OR", "NOR", "NAND"]: #checkt of het wel een goede gate is
                layer.append(p.gateUnderstander(gate)) #zet het in een list genaamd layer
            else: #anders stop alles en zeg dat het niet goed is
                print("Gate or Entire Input wrongly typed")
                print(layer)
                break

    def __str__(self):
        listsOfGates = []
        for i in self.layer:
            listsOfGates.append(i)
        return listsOfGates #waarschijnlijk wilde ik hier ene list terug geven van alle gates, maar dat is niet goed gegaan