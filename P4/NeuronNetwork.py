from . import NeuronLayer as neulay
import random

class NeuronNetwork:
    layer = None

    def __init__(self, networkStructure):
        self.networkStructure = networkStructure
        return

    def feed_forward(self, networkInput):
        """

        :param networkInput: a list with the input which could be [0,0] and will be used in the beginning of the network
        :return: the output of the network which is calculated by layer (which has calculated from network)
        """
        self.networkInput = networkInput
        allLayerOutputs = []
        for layerindex in range(len(self.network_weights)):
            neuronLayer = neulay.NeuronLayer()
            neuronLayeroutput = neuronLayer.get_layer_output(self.network_weights[layerindex], self.network_bias[layerindex], networkInput)

            allLayerOutputs.append(neuronLayeroutput)
            neuronLayer.__str__()
            networkInput = neuronLayer.__iter__()

        self.output = neuronLayer.__iter__()

        return neuronLayer.__iter__()

    def get_network_error(self, target, output):
        """
        :param target: a list with numbers, which indicate the right answers
        :param output: a list with numbers, which has numbers that are calculated by feedforward
        calculate for every gate in every layer the difference between target and output using the formula's
        :return:
        - a list of the gate errors which have the same place/index as the netwerk structure itself. E.G. [[0.2, 0.4], [0.1]] in a network structure [[AND, AND], [AND]
        - a list of the gate output (activations) which have the same place/index as the netwerk structure itself. E.G. [[0.2, 0.4], [0.1]] in a network structure [[AND, AND], [AND]
        """
        outputlayerStructure = self.networkStructure[-1].copy()
        hiddenlayersStructure = list(self.networkStructure[0:-1]).copy()
        errorStructure = self.networkStructure.copy()
        activationStructure = self.networkStructure.copy()
        activationStructure[-1] = output
        for outputLayerIndex in range(len(outputlayerStructure)): #looping through neurons
            neuronLayer = neulay.NeuronLayer()
            error = neuronLayer.get_outputlayer_error(target[outputLayerIndex], output[outputLayerIndex])
            errorStructure[-1][outputLayerIndex] = error

        for hiddenLayerIndex in range(len(hiddenlayersStructure)): #looping through layers
            neuronLayer = neulay.NeuronLayer()
            neuronLayeroutput = neuronLayer.get_layer_output(self.network_weights[hiddenLayerIndex], self.network_bias[hiddenLayerIndex], self.networkInput)
            activationStructure[hiddenLayerIndex] = neuronLayeroutput
            hiddenerror = neuronLayer.get_hiddenlayer_error(self.network_weights, errorStructure, neuronLayeroutput, hiddenlayersStructure, hiddenLayerIndex)
            errorStructure[hiddenLayerIndex] = hiddenerror
            # print("errorStructure", errorStructure)
        return errorStructure, activationStructure

    def network_backpropagation(self, error_structure, activation_structure, inputs, learningrate=1):
        """
        Uses the error_structure, activation_structure and learningrate to change the weights and bias for the output
        and after that +inputs to also calculte the new weights and biases for the hiddenlayers
        :param error_structure: a list of the gate errors which have the same place/index as the netwerk structure itself. E.G. [[0.2, 0.4], [0.1]] in a network structure [[AND, AND], [AND]
        :param activation_structure: a list of the gate output (activations) which have the same place/index as the netwerk structure itself. E.G. [[0.2, 0.4], [0.1]] in a network structure [[AND, AND], [AND]
        :param inputs: a list with the input which could be [0,0] and will be used in the beginning of the network
        :param learningrate: the amount of change every time it changes weights and bias. Default on 1
        :self It saves the new bias and weights in the class with self. so it easily can be summoned if needed
        """
        new_weight_structure = self.network_weights.copy()
        new_bias_structure = self.network_bias.copy()
        for outputNeuronIndex in range(len(self.network_weights[-1])):
            for outputNeuronWeightIndex in range(len(self.network_weights[-1][outputNeuronIndex])):
                    new_weight_structure[-1][outputNeuronIndex][outputNeuronWeightIndex] = new_weight_structure[-1][outputNeuronIndex][outputNeuronWeightIndex] - learningrate * activation_structure[-2][outputNeuronWeightIndex] * error_structure[-1][outputNeuronIndex]


            new_bias_structure[-1][outputNeuronIndex] = new_bias_structure[-1][outputNeuronIndex] - learningrate * error_structure[-1][outputNeuronIndex]
        for hiddenLayerIndex in range(len(self.network_weights[:-1])):
            for hiddenNeuronIndex in range(len(self.network_weights[:-1][hiddenLayerIndex])):
                for hiddenNeuronWeightIndex in range(len(self.network_weights[:-1][hiddenLayerIndex][hiddenNeuronIndex])):
                    try:
                        new_weight_structure[:-1][hiddenLayerIndex][hiddenNeuronIndex][hiddenNeuronWeightIndex] = new_weight_structure[:-1][hiddenLayerIndex][hiddenNeuronIndex][hiddenNeuronWeightIndex] - learningrate *  activation_structure[hiddenLayerIndex-1][hiddenNeuronIndex][hiddenNeuronWeightIndex] * error_structure[hiddenLayerIndex][hiddenNeuronIndex]
                    except (TypeError, IndexError) as e:
                        new_weight_structure[:-1][hiddenLayerIndex][hiddenNeuronIndex][hiddenNeuronWeightIndex] = new_weight_structure[:-1][hiddenLayerIndex][hiddenNeuronIndex][hiddenNeuronWeightIndex] - learningrate * inputs[hiddenNeuronWeightIndex] * error_structure[hiddenLayerIndex][hiddenNeuronIndex]

                new_bias_structure[hiddenLayerIndex][hiddenNeuronIndex] = new_bias_structure[hiddenLayerIndex][hiddenNeuronIndex] - learningrate * error_structure[hiddenLayerIndex][hiddenNeuronIndex]
        self.network_weights  = new_weight_structure
        self.network_bias =  new_bias_structure

    def set_network_weights(self, network_weights=None):
        """
        returns network_weights
        :param network_weights: a list of the gate weights which have the same place/index as the netwerk structure itself. E.G. [[0.2, 0.4], [0.1]] in a network structure [[AND, AND], [AND]
        """
        if network_weights == None:
            tempNetwork_weights = []
            for layer in self.networkStructure:
                tempLayer_weights = []
                for neuron in layer:
                    tempLayer_weights.append([random.uniform(1, 2), random.uniform(1, 2)])
                tempNetwork_weights.append(tempLayer_weights)
            network_weights = tempNetwork_weights
            print(network_weights)
        self.network_weights = network_weights

    def set_network_bias(self, network_bias=None):
        """
        returns network_bias
        :param network_bias: a list of the gate biases which have the same place/index as the netwerk structure itself. E.G. [[0.2, 0.4], [0.1]] in a network structure [[AND, AND], [AND]
        """
        if network_bias == None:
            tempNetwork_bias = []
            for layer in self.networkStructure:
                tempLayer_bias = []
                for neuron in layer:
                    tempLayer_bias.append(random.uniform(1, 2))
                tempNetwork_bias.append(tempLayer_bias)
            network_bias = tempNetwork_bias
        self.network_bias = network_bias

    def get_network_weights(self):
        return self.network_weights

    def get_network_bias(self):
        return self.network_bias

    def __str__(self):
        return "With input: " + str(self.networkInput) + " Gives: " + str(self.output[0]) + "\n"