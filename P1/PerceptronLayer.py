import Perceptron as per

class PerceptronLayer:
    layer = None
    def __init__(self, gatesInLayer, listOfAmountOfInputs): #vraagt op de gatesindelayer en welk naam ze hebben (misschien moet ik de layer nummer er bij zetten)
        """
        Vraagt uit de input de string gates op en vraagt in Perceptron.py met de gateunderstander de juiste perceptron.
        Daarnaast bij gebruik van meerdere gates in 1 layer, worden de resultaten samen in 1 input gezet (omdat ze toch hetzelfde zijn)
        -Zet de default perceptron op lege weights en bias
        -Loopt door alle gates van de inputs
        -Checkt of de gates goed zijn ingevoerd
        -Voert elke gate in de gateunderstander van perceptron.py om de perceptron op te vragen en het in een layer toe te voegen
        -De "for x in range(len(layer))" zorgt voor de uitkomsten, bij het gebruik van meerdere gates in een layer, samen in de value
        dictionary komen om het overzichtelijker te maken voor gebruikers en makkelijker waardes eruit te halen voor de volgende laag
        :param
        :rtype: object
        """
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
            if x == 0: #als het de eerste is in de layer, voeg dan toe als list
                listsOfGatesinLayer.append(layer[x].activation())
            else: #zo niet voeg dan het als een cijfer toe aan de al bestaande output list
                Outputlist = layer[x].activation()
                for key, value in Outputlist.items():
                    listsOfGatesinLayer[0][key].append(value[0])
        listsOfGatesinLayer = listsOfGatesinLayer[0] #voorkomt het onnodig gebruik van een extra list om de dictionary
        self.listsOfGatesinLayer = listsOfGatesinLayer
        self.layer = layer

    def __dict__(self):
        return self.listsOfGatesinLayer #waarschijnlijk wilde ik hier ene list terug geven van alle gates, maar dat is niet goed gegaan

'''PRINT OM STANDAARD GATES TE GEBRUIKEN IN 1 LAYER'''
# pl = PerceptronLayer(["NAND", "OR", "INVERT"], [2, 2, 1])
# print(pl)

# pl = PerceptronLayer(["OR", "NAND"], [2, 2])
# print(pl)
