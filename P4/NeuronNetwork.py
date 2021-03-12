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
            hiddenerror = neuronLayer.get_bighiddenlayer_error(self.network_weights, errorStructure, neuronLayeroutput, hiddenlayersStructure, hiddenLayerIndex)
            errorStructure[hiddenLayerIndex] = hiddenerror
            # print("errorStructure", errorStructure)
        return errorStructure, activationStructure

    def get_bignetwork_error(self, target, output):
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
            hiddenerror = neuronLayer.get_bighiddenlayer_error(self.network_weights, errorStructure, neuronLayeroutput, hiddenlayersStructure, hiddenLayerIndex)
            errorStructure[hiddenLayerIndex] = hiddenerror

        return errorStructure, activationStructure

    def network_backpropagation(self, error_structure, activation_structure, inputs, learningrate=0.1):
        # print("\nactivation_structure", activation_structure,  "\nerror_structure ", error_structure)
        new_weight_structure = self.network_weights.copy()
        new_bias_structure = self.network_bias.copy()
        ''' TODO: Get output layer new weights and bias'''
        for outputNeuronIndex in range(len(self.network_weights[-1])):
            for outputNeuronWeightIndex in range(len(self.network_weights[-1][outputNeuronIndex])):
                 # print("W:", self.network_weights[-1][outputNeuronIndex][outputNeuronWeightIndex])
                 # print("A:", activation_structure[-2][outputNeuronWeightIndex])
                 # print("learingrate:", learningrate)
                 # print("Delta:", error_structure[-1][outputNeuronIndex])
                    new_weight_structure[-1][outputNeuronIndex][outputNeuronWeightIndex] = new_weight_structure[-1][outputNeuronIndex][outputNeuronWeightIndex] - learningrate * activation_structure[-2][outputNeuronWeightIndex] * error_structure[-1][outputNeuronIndex]


            new_bias_structure[-1][outputNeuronIndex] = new_bias_structure[-1][outputNeuronIndex] - learningrate * error_structure[-1][outputNeuronIndex]
                # print("outputlayerStructure", self.outputlayerStructure[NeuronIndex])
        ''' TODO: Get hidden layers new weights and bias (reversed)'''
        Layerlength = len(self.network_weights[:-1])
        for hiddenLayerIndex in range(len(self.network_weights[:-1])):
            for hiddenNeuronIndex in range(len(self.network_weights[:-1][hiddenLayerIndex])):
                for hiddenNeuronWeightIndex in range(len(self.network_weights[:-1][hiddenLayerIndex][hiddenNeuronIndex])):
                    # print(self.network_weights[:-1][hiddenLayerIndex][hiddenNeuronIndex][hiddenNeuronWeightIndex])

                    try:
                        # print("W:", new_weight_structure[:-1][hiddenLayerIndex][hiddenNeuronIndex][hiddenNeuronWeightIndex])
                        # print("A short:", activation_structure[hiddenLayerIndex-1])
                        # print("A:", activation_structure[hiddenLayerIndex-1][hiddenNeuronIndex][hiddenNeuronWeightIndex])
                        # print("learningrate:", learningrate)
                        # print("Delta:", error_structure[hiddenLayerIndex][hiddenNeuronIndex])
                        new_weight_structure[:-1][hiddenLayerIndex][hiddenNeuronIndex][hiddenNeuronWeightIndex] = new_weight_structure[:-1][hiddenLayerIndex][hiddenNeuronIndex][hiddenNeuronWeightIndex] - learningrate *  activation_structure[hiddenLayerIndex-1][hiddenNeuronIndex][hiddenNeuronWeightIndex] * error_structure[hiddenLayerIndex][hiddenNeuronIndex]
                    except (TypeError, IndexError) as e:
                        # print("Not good A:", inputs[hiddenNeuronWeightIndex], inputs)
                        # print("learningrate:", learningrate)
                        # print("Delta:", error_structure[hiddenLayerIndex][hiddenNeuronIndex])
                        new_weight_structure[:-1][hiddenLayerIndex][hiddenNeuronIndex][hiddenNeuronWeightIndex] = new_weight_structure[:-1][hiddenLayerIndex][hiddenNeuronIndex][hiddenNeuronWeightIndex] - learningrate * inputs[hiddenNeuronWeightIndex] * error_structure[hiddenLayerIndex][hiddenNeuronIndex]

                new_bias_structure[hiddenLayerIndex][hiddenNeuronIndex] = new_bias_structure[hiddenLayerIndex][hiddenNeuronIndex] - learningrate * error_structure[hiddenLayerIndex][hiddenNeuronIndex]

        # print("new_weight_structure", new_weight_structure)
        # print("new_bias_structure", new_bias_structure)
        self.network_weights  = new_weight_structure
        self.network_bias =  new_bias_structure

    def set_network_weights(self, network_weights=None):
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