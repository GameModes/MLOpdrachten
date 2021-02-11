import Perceptron as per

class PerceptronLayer:
    def __init__(self, gatesInLayer, gateNames):
        self.layer = None
        layer = []
        p = per.Perceptron(weights=[], bias=0) #default
        for gate in gatesInLayer[0]: #
            if gate in ["INVERT", "AND", "OR", "NOR", "NAND"]:
                layer.append(p.gateUnderstander(gate))
            else:
                print("Gate or Entire Input wrongly typed")
                print(layer)
                break

    def __str__(self):
        listsOfGates = []
        for i in self.layer:
            listsOfGates.append(i)
        return listsOfGates