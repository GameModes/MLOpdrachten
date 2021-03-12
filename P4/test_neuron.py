
# import Neuron as neur
from unittest import TestCase

from . import NeuronNetwork as neurNet
from sklearn.datasets import load_iris
import numpy as np
from progress.bar import Bar
import importlib


class TestNeuron(TestCase):
    def neuronTester(self, tests, targets, port):
        global output
        decimals = 10
        decimalscorrect = 0
        for n in range(1):
            for i in range(len(tests)):
                for n in range(decimals):
                    try:
                        output = port.get_gate_output(tests[i])
                        self.assertAlmostEqual(targets[i], output , n)
                    except AssertionError:
                        decimalscorrect =  n
                        break
                print("Test:", tests[i], "Target:", targets[i], "With Weights:", port.get_weights(), "With Bias:", port.get_bias() , "Output:" , output, "Decimals correct: ", decimalscorrect)
                error = port.get_error(targets[i], output)
                newWeightslist, newBias = port.backpropagation(error, tests[i], learningrate=1)



        print('--------------------------------------------------------------------------------------------\n')
        return output

    def networkTester(self, tests, targets, port):
        global output
        firstoutput = port.feed_forward(tests[0])
        print("First Test:", tests[0], "Target:", targets[0], "Output:", firstoutput, "\nBias: ", port.get_network_bias(), "\nWeights:", port.get_network_weights())
        for n in range(10000):
            for i in range(len(tests)):
                output = port.feed_forward(tests[i])
                # print("Test:", tests[i], "Target:", targets[i], "Output:", output, "\nBias: ", port.get_network_bias(), "\nWeights:", port.get_network_weights())
                error_structure, activation_structure = port.get_network_error(targets[i], output)
                port.network_backpropagation(error_structure, activation_structure, tests[i], 1)  # vergeet niet learningrate toe te voegen

        print("\nLast Test:", tests[i], "Target:", targets[i], "Output:", output, "\nBias: ", port.get_network_bias(), "\nWeights:", port.get_network_weights())
        print('--------------------------------------------------------------------------------------------\n')


    def bignetworkTester(self, tests, targets, port):
        global output
        firstoutput = port.feed_forward(tests[0])
        print("First Test:", tests[0], "Target:", targets[0], "Output:", firstoutput, "\nBias: ", port.get_network_bias(), "\nWeights:", port.get_network_weights())
        for n in range(1000):
            for i in range(len(tests)):
                output = port.feed_forward(tests[i])
                # print("Test:", tests[i], "Target:", targets[i], "Output:" , output, "\nBias: ", port.get_network_bias(),"\nWeights:", port.get_network_weights())
                error_structure, activation_structure = port.get_bignetwork_error(targets[i], output)
                port.network_backpropagation(error_structure, activation_structure, tests[i], 1)  # vergeet niet learningrate toe te voegen
        print("\nLast Test:", tests[i], "Target:", targets[i], "Output:", output, "\nBias: ", port.get_network_bias(), "\nWeights:", port.get_network_weights())
        print('--------------------------------------------------------------------------------------------\n')

    def test_edited_halfAdder(self):
        print('Half Adder Port:')            #f             g           h       s           c
        half_Adder = neurNet.NeuronNetwork([["OR_port", "NAND_port", "AND"], ["AND_port", "AND_port"]])
        half_Adder.set_network_weights(    [[ [0, 0.1]  ,[0.2, 0.3], [0.4, 0.5]], [[0.6, 0.7, 0.8,], [0.9, 1, 1.1] ]])
        half_Adder.set_network_bias([[0, 0, 0], [0, 0]])
        tests = [[1, 1], [0, 1], [1, 0], [0, 0]]
        target = [[0, 1], [1,0], [1,0], [0,0]]
        self.networkTester(tests, target, half_Adder)

    # def test_edited_XOR(self):
    #     print("Test XOR:")
    #     XOR_port = neurNet.NeuronNetwork([["OR_port", "NAND_port"], ["AND_port"]])
    #     XOR_port.set_network_weights(    [[ [0.2, -0.4]  ,[0.7, 0.1]], [[0.6, 0.9] ]])
    #     XOR_port.set_network_bias([[0, 0], [0]])
    #     XOR_port.feed_forward([1,0])
    #     tests = [[1, 1], [0, 1], [1, 0], [0, 0]]
    #     target = [[0], [1], [1], [0]]
    #     self.networkTester(tests, target, XOR_port)

    def test_edited_XOR(self):
        print("Test XOR:")
        XOR_port = neurNet.NeuronNetwork([["OR_port", "NAND_port"], ["AND_port"]])
        XOR_port.set_network_weights(    [[ [1, 1]  ,[-1, -1]], [[2, 2] ]])
        XOR_port.set_network_bias([[-1, 4], [-4]])
        XOR_port.feed_forward([1,0])
        tests = [[1, 1], [0, 1], [1, 0], [0, 0]]
        target = [[0], [1], [1], [0]]
        self.networkTester(tests, target, XOR_port)

    # def test_XOR(self):
    #     print("XOR:")
    #     XOR_port = neurNet.NeuronNetwork([["OR_port", "NAND_port"], ["AND_port"]])
    #     XOR_port.set_network_weights(    [[ [4, 4]  ,[-2.5, -2.5]], [[4.5, 4.5] ]])
    #     XOR_port.set_network_bias([[-2, 4.5], [-7.5]])
    #     XOR_port.feed_forward([1,0])
    #     tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     target = [[0], [1], [1], [0]]
    #     self.networkTester(tests, target, XOR_port)

    # def test_INVERT(self):
    #     INVERT_port = neur.Neuron(weights=[-1], bias=0.5)
    #     self.INVERT_port = INVERT_port
    #     tests = [[0], [1]]
    #     target = [1, 0]
    #     print("Invert:")
    #     self.neuronTester(tests, target, INVERT_port)

    # def test_adjusted_INVERT(self):
    #     INVERT_port = neur.Neuron(weights=[-100], bias=10)
    #     self.INVERT_port = INVERT_port
    #     tests = [[0], [1]]
    #     target = [1, 0]
    #     print("Adj Invert:")
    #
    #     self.neuronTester(tests, target, INVERT_port)


    # def test_AND(self):
    #     AND_port = neur.Neuron(weights=[0.5, 0.5], bias=-1)
    #     self.AND_port = AND_port
    #     tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     target = [0, 0, 0, 1]
    #     print("AND:")
    #     self.neuronTester(tests, target, AND_port)

    # def test_adjusted_AND(self):
    #     AND_port = neur.Neuron(weights=[4.5, 4.5], bias=-7.5)
    #     self.AND_port = AND_port
    #     tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     target = [0, 0, 0, 1]
    #     print("Adj AND:")
    #     # for n in range(10000):
    #     self.neuronTester(tests, target, AND_port)

    # def test_OR(self):
    #     OR_port = neur.Neuron(weights=[0.5, 0.5], bias=-0.5)
    #     self.OR_port = OR_port
    #     tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     target = [0, 1, 1, 1]
    #     print("OR:")
    #     self.neuronTester(tests, target, OR_port)
    #
    # def test_adjusted_OR(self):
    #     OR_port = neur.Neuron(weights=[4, 4], bias=-2)
    #     self.OR_port = OR_port
    #     tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     target = [0, 1, 1, 1]
    #     print("Adj OR:")
    #     self.neuronTester(tests, target, OR_port)
    #
    # def test_NOR(self):
    #     NOR_port = neur.Neuron(weights=[-0.5, -0.5], bias=0)
    #     self.NOR_port = NOR_port
    #     tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     target = [1, 0, 0, 0]
    #     print("NOR:")
    #     self.neuronTester(tests, target, NOR_port)
    #
    # def test_adjusted_NOR(self):
    #     NOR_port = neur.Neuron(weights=[-4, -4], bias=2)
    #     self.NOR_port = NOR_port
    #     tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     target = [1, 0, 0, 0]
    #     print("Adj NOR:")
    #     self.neuronTester(tests, target, NOR_port)
    #
    # def test_party(self):
    #     Party_port = neur.Neuron(weights=[0.6, 0.3, 0.2], bias=-0.4)
    #     self.Party_port = Party_port
    #     tests = [[0, 0, 0 ], [0, 1, 0], [1, 0, 0], [1, 1,0], [0, 0, 1 ], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
    #     target = [0, 0, 1, 1, 0, 1, 1, 1]
    #     print("Party:")
    #     self.neuronTester(tests, target, Party_port)
    #
    # def test_adjusted_party(self):
    #     Party_port = neur.Neuron(weights=[4, 2, 2], bias=-3)
    #     self.Party_port = Party_port
    #     tests = [[0, 0, 0 ], [0, 1, 0], [1, 0, 0], [1, 1,0], [0, 0, 1 ], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
    #     target = [0, 0, 1, 1, 0, 1, 1, 1]
    #     print("Adj Party:")
    #     self.neuronTester(tests, target, Party_port)
    #
    # def test_NAND(self):
    #     NAND_port = neur.Neuron(weights=[-0.5, -0.5], bias=0.5)
    #     self.NAND_port = NAND_port
    #     tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     target = [1, 1, 1, 0]
    #     print("NAND:")
    #     self.neuronTester(tests, target, NAND_port)
    #
    # def test_adjusted_NAND(self):
    #     NAND_port = neur.Neuron(weights=[-2.5, -2.5], bias=4.5)
    #     self.NAND_port = NAND_port
    #     tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     target = [1, 1, 1, 0]
    #     print("Adj NAND:")
    #     self.neuronTester(tests, target, NAND_port)
    #



    # def test_halfAdder(self):
    #     print('Half Adder Port:')
    #     half_Adder = neurNet.NeuronNetwork([["OR_port", "NAND_port", "AND"], ["AND_port", "AND_port"]])
    #     half_Adder.set_network_weights(    [[ [4.0, 4.0]  ,[-2.5, -2.5], [4.5, 4.5]], [[4.5, 4.5, 4.5,], [-2.5, -2.5, -2.5] ]])
    #     half_Adder.set_network_bias([[-2, 4.5, -7.5], [-7.5, -2]])
    #     tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
    #     target = [[0, 0], [0,1], [0,1], [1,0]]
    #     self.networkTester(tests, target, half_Adder)
