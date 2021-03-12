from typing import List
class Neuron:
    layer = None

    def __init__(self, weights: List[float], bias: float):
        self.bias = bias
        self.weights = weights

    def get_gate_output(self, inputs=None):  # source: https://www.simplilearn.com/what-is-perceptron-tutorial#:~:text=Sigmoid%20Activation%20Function,-The%20diagram%20given&text=This%20is%20called%20a%20logistic,zero%20for%20highly%20negative%20input.
        """

        :param inputs: a list with number which indicates which weights should be (how much) activated
        Extra param:
        self.bias, before getting a positive answer, the answer must be above this value
        self.weights, the weight indicates how much every input does and gives to the output
        :return: a value between 0 and 1 which is calculated by sigmoid which indicate how much a gate is on(1) or off(0)
        """
        if inputs is None:
            inputs = [0, 0]

        netinput = self.bias
        try:

            for index in range(len(inputs)):
                netinput += inputs[index] * self.weights[index]
            netoutput = 1 / (1 + 2.71828 ** -netinput)  # source for 2.71828: https://en.wikipedia.org/wiki/E_(mathematical_constant)

            self.netoutput = netoutput
        except IndexError:
            netinput = self.bias
            for index in range(len(inputs[:2])):
                netinput += inputs[index] * self.weights[index]
            netoutput = 1 / (1 + 2.71828 ** -netinput)  # source for 2.71828: https://en.wikipedia.org/wiki/E_(mathematical_constant)
            self.netoutput =  inputs[2:] + [netoutput]

        #         print(netoutput)

        return self.netoutput

    def backpropagation(self, a,  inputlist, learningrate):
        newWeightslist = [self.weights[index] - learningrate * inputlist[index] * a for index, x in enumerate(self.weights)]
        newBias = self.bias - learningrate * 1 * a
        self.bias = newBias
        self.weights = newWeightslist
        return newWeightslist, newBias

    def get_error(self, target, a):
        return a * (1-a) * -(target-a)

    def get_hidden_error(self, SumOfNextLayer, a):
        return a * (1-a) * SumOfNextLayer


    def get_weights(self):
        return self.weights

    def get_bias(self):
        return self.bias

    def __str__(self):
        """
        :return: if needed this will return the rounded value of the neuron netoutput
        """
        if self.netoutput >= 0.5:
            trueoutput = 1
        else:
            trueoutput = 0
        return str(trueoutput)
