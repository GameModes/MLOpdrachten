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
        """
        :param target: the predicted value of the output of the outputlayer
        :param output: the true value of the output of the outputlayer
        :return: the delta error calculated from Neuron.py
        """
        test_neuron = neur.Neuron([0, 0], 0)
        delta = test_neuron.get_error(target, output)
        return delta

    def get_hiddenlayer_error(self, weights, errorStructure, output, hiddenlayersStructure, hiddenLayerIndex, ):
        """
        :param weights:a list of the gate weights which have the same place/index as the netwerk structure itself. E.G. [[0.2, 0.4], [0.1]] in a network structure [[AND, AND], [AND]
        :param errorStructure: a list of the gate errors which have the same place/index as the netwerk structure itself. E.G. [[0.2, 0.4], [0.1]] in a network structure [[AND, AND], [AND]
        :param output: the output of the network
        :param hiddenlayersStructure: the network structure but only the hiddenlayers (no outputlayers)
        :param hiddenLayerIndex: the index number of the hiddenlayerstructure that is selected to use/calculate the error
        :return: a list with all the error/delta numbers of all gates in the selected hiddenlayer
        """
        errorLayerList = []
        for hiddenNeuronIndex in range(len(hiddenlayersStructure[hiddenLayerIndex])): #Looping through neurons in layerlist
            contributedWeightsList = [weight_of_next[hiddenNeuronIndex] for weight_of_next in weights[hiddenLayerIndex + 1]]
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
        return str(trueOutputlist)