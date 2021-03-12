from . import Neuron as neur

class NeuronLayer:
    layer = None

    def get_layer_output(self, weights, bias, input):
        """
        :param weights: a list with all the neuron's weights in that layer
        :param bias: a list with all the neuron's bias in that layer
        :param input: the input which will be used as a parameter for get_gate_output
        :self gatesLayerOutputList: a list which contain every output of gates in that layer
        """
        gatesLayerOutputList = []
        for neuronIndex in range(len(weights)):

            neuron = neur.Neuron(weights[neuronIndex], bias[neuronIndex])
            output = neuron.get_gate_output(input)
            if isinstance(output, float):
                gatesLayerOutputList.append(neuron.get_gate_output(input))
            else:
                gatesLayerOutputList = output
        self.gatesLayerOutputList = gatesLayerOutputList
        return gatesLayerOutputList

    def get_outputlayer_error(self, target, output):
        test_neuron = neur.Neuron([0, 0], 0)
        delta = test_neuron.get_error(target, output)
        return delta

    def get_bighiddenlayer_error(self, weights, errorStructure, output, hiddenlayersStructure, hiddenLayerIndex, ):
        errorLayerList = []
        # print("weights", weights)
        # print("hiddenlayersStructure:", hiddenlayersStructure)
        for hiddenNeuronIndex in range(len(hiddenlayersStructure[hiddenLayerIndex])): #Looping through neurons in layerlist
            contributedWeightsList = [weight_of_next[hiddenNeuronIndex] for weight_of_next in weights[hiddenLayerIndex + 1]]

            contributedErrorList = [error_of_next for error_of_next in errorStructure[hiddenLayerIndex + 1]]
            sumInNextLayer = 0
            for i in range(len(contributedErrorList)):
                sumInNextLayer += contributedErrorList[i] * contributedWeightsList[i]
            test_neuron = neur.Neuron([0, 0], 0)
            error = test_neuron.get_hidden_error(sumInNextLayer, output[hiddenNeuronIndex])
            errorLayerList.append(error)
        # print("errorStructure: ", errorStructure, "errorLayerList: ", errorLayerList)
        return errorLayerList

    def get_hiddenlayer_error(self, weights, errorStructure, output, hiddenlayersStructure, hiddenLayerIndex, ):
        errorLayerList = []
        for hiddenNeuronIndex in range(len(hiddenlayersStructure[hiddenLayerIndex])): #Looping through neurons in layerlist
            contributedWeightsList = [weight_of_next[hiddenNeuronIndex] for weight_of_next in weights[hiddenLayerIndex + 1]]
            print(contributedWeightsList)
            contributedErrorList = [error_of_next for error_of_next in errorStructure[hiddenLayerIndex + 1]]
            sumInNextLayer = 0
            for i in range(len(contributedErrorList)):
                sumInNextLayer += contributedErrorList[i] * contributedWeightsList[i]
            test_neuron = neur.Neuron([0, 0], 0)
            error = test_neuron.get_hidden_error(sumInNextLayer, output[hiddenNeuronIndex])
            errorLayerList.append(error)
        return errorLayerList

    def __iter__(self):
        return self.gatesLayerOutputList

    def __str__(self):
        trueOutputlist = self.gatesLayerOutputList
        #         for x in range(len(trueOutputlist)):
        #             if trueOutputlist[x] >= 0.5:
        #                 trueOutputlist[x] = 1
        #             else:
        #                 trueOutputlist[x] = 0
        return str(trueOutputlist)