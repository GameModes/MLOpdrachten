from unittest import TestCase

from sklearn import datasets

from . import Neuron as neur
from . import NeuronNetwork as neurNet
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error, accuracy_score

class TestNeuron(TestCase):
    def neuronTester(self, tests, targets, port, learningrate=1, amountOfEpochsLooping = 10000):
        global output
        decimals = 10
        decimalscorrect = 0
        y_true = []
        if len(tests) <= 20:
            for i in range(len(tests)):
                firstoutput = port.get_gate_output(tests[i])
                print("First Test:", tests[i], "Target:", targets[i], "Output:", firstoutput)
        else:
            print("List is too big to show")
        print("\nBias: ", port.get_bias(), "\nWeights:", port.get_weights())
        print("\n*Testing Time....*\n")
        for amount in range(amountOfEpochsLooping+1):
            for i in range(len(tests)):
                for n in range(decimals):
                    try:
                        output = port.get_gate_output(tests[i])
                        self.assertAlmostEqual(targets[i], output , n)
                    except AssertionError:
                        decimalscorrect =  n
                        break
                error = port.get_error(targets[i], output)
                newWeightslist, newBias = port.backpropagation(error, tests[i], learningrate)
                if amount == amountOfEpochsLooping:
                    if len(tests) <= 20:
                        print("Last Test:", tests[i], "Target:", targets[i], "Output:", output, "Decimals correct: ", decimalscorrect)
                    y_true.append(output)

        print("\nAfter ", amountOfEpochsLooping, " Times:\nBias: ", port.get_bias(), "\nWeights:", port.get_weights(), "\nMSE: ", mean_squared_error(y_true, targets), "Accuracy:", accuracy_score([round(num) for num in y_true], targets , normalize=False), " of ", len(targets))
        print('--------------------------------------------------------------------------------------------\n')
        return output

    def networkTester(self, tests, targets, port, learningrate=1, amountOfEpochsLooping=10000):
        global output
        ListIsTooBig = False
        for i in range(len(tests)):
            firstoutput = port.feed_forward(tests[i])
            if len(tests) <= 20:
                print("First Test:", tests[i], "Target:", targets[i], "Output:", firstoutput)
            else:
                ListIsTooBig = True
        if ListIsTooBig:
            print(firstoutput)
            print("List is too big to show")
        print("\nBias: ", port.get_network_bias(), "\nWeights:", port.get_network_weights())
        print("\n*Testing Time....*\n")
        for n in range(amountOfEpochsLooping+1):
            for i in range(len(tests)):
                output = port.feed_forward(tests[i])
                error_structure, activation_structure = port.get_network_error(targets[i], output)
                port.network_backpropagation(error_structure, activation_structure, tests[i], learningrate)
                if n == amountOfEpochsLooping:
                    print("Last Test:", tests[i], "Target:", targets[i], "Output:", output)
        print("\nAfter ",  amountOfEpochsLooping, " Times:\nBias: ", port.get_network_bias(), "\nWeights:", port.get_network_weights())
        print('--------------------------------------------------------------------------------------------\n')

    def test_AND(self):
        AND_port = neur.Neuron(weights=[-0.5, 0.5], bias=1.5)
        self.AND_port = AND_port
        tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
        target = [0, 0, 0, 1]
        print("AND:")
        self.neuronTester(tests, target, AND_port, 1, 1000)

    def test_IrisDataset(self):
        ''' I realised I need to be able to use a network with only 3 output layers
        I had no time to fix it, for today unfortunate
        '''
        Iris_tests = load_iris().get('data')
        target_array = load_iris().get('target')
        target_array2 = []
        for i in range(len(target_array)):
            lijst = [0, 0, 0]
            lijst[target_array[i]] = 1
            target_array2.append(lijst)
        print('exerciseBook Iris Dataset Port:')            #f             g           h       s           c
        IrisDataset = neurNet.NeuronNetwork([["AND_port", "AND_port", "AND_port"]])
        IrisDataset.set_network_weights(    [[[0.6, 0.7, 0.8], [0.9, 1, 1.1], [0.9, 1, 1.1]]])
        IrisDataset.set_network_bias([[0, 0, 0]])
        self.networkTester(Iris_tests, target_array2, IrisDataset)


    # def test_DigitDataset(self):
    #
    #     Digit_tests = datasets.load_digits().get('data')
    #     target_array = datasets.load_digits().get('target')
    #     Digit_tests = [x / 16 for x in Digit_tests]
    #     IrisDataset = neur.Neuron(weights=[0.5, 0.5, 0.5, 0.5], bias=-1)
    #     self.neuronTester(Iris_tests, target_array, IrisDataset, learningrate=1, amountOfEpochsLooping=4)
    #
    #     Iris_tests = load_iris().get('data')
    #     target_array = load_iris().get('target')
    #     targets = [1 if x == 2 else x for x in target_array]
    #     print('IrisDataset:')
    #     IrisDataset = neur.Neuron(weights=[0.5, 0.5, 0.5, 0.5], bias=-1)
    #     self.neuronTester(Iris_tests, targets, IrisDataset, learningrate=1, amountOfEpochsLooping=4)

    def test_exerciseBook_halfAdder(self):
        print('exerciseBook Half Adder Port:')            #f             g           h       s           c
        half_Adder = neurNet.NeuronNetwork([["OR_port", "NAND_port", "AND"], ["AND_port", "AND_port"]])
        half_Adder.set_network_weights(    [[ [0, 0.1]  ,[0.2, 0.3], [0.4, 0.5]], [[0.6, 0.7, 0.8,], [0.9, 1, 1.1] ]])
        half_Adder.set_network_weights([[[0, 0.1], [0.2, 0.3], [0.4, 0.5]], [[0.6, 0.7, 0.8, ], [0.9, 1, 1.1]]])
        half_Adder.set_network_bias([[0, 0, 0], [0, 0]])
        tests = [[1, 1], [0, 1], [1, 0], [0, 0]]
        target = [[0, 1], [1,0], [1,0], [0,0]]
        self.networkTester(tests, target, half_Adder)

    def test_exerciseBook_XOR(self):
        print("exerciseBook XOR:")
        XOR_port = neurNet.NeuronNetwork([["OR_port", "NAND_port"], ["AND_port"]])
        XOR_port.set_network_weights(    [[ [0.2, -0.4]  ,[0.7, 0.1]], [[0.6, 0.9] ]])
        XOR_port.set_network_bias([[0, 0], [0]])
        XOR_port.feed_forward([1,0])
        tests = [[1, 1], [0, 1], [1, 0], [0, 0]]
        target = [[0], [1], [1], [0]]
        self.networkTester(tests, target, XOR_port)

    def test_manual_XOR(self):
        print("Manual XOR:")
        XOR_port = neurNet.NeuronNetwork([["OR_port", "NAND_port"], ["AND_port"]])
        XOR_port.set_network_weights(    [[ [1, 1]  ,[-1, -1]], [[2, 2] ]])
        XOR_port.set_network_bias([[-1, 4], [-4]])
        XOR_port.feed_forward([1,0])
        tests = [[1, 1], [0, 1], [1, 0], [0, 0]]
        target = [[0], [1], [1], [0]]
        self.networkTester(tests, target, XOR_port)

    def test_ManualAdjusted_XOR(self):
        print("Adj XOR:")
        XOR_port = neurNet.NeuronNetwork([["OR_port", "NAND_port"], ["AND_port"]])
        XOR_port.set_network_weights(    [[ [4, 4]  ,[-2.5, -2.5]], [[4.5, 4.5] ]])
        XOR_port.set_network_bias([[-2, 4.5], [-7.5]])
        XOR_port.feed_forward([1,0])
        tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
        target = [[0], [1], [1], [0]]
        self.networkTester(tests, target, XOR_port)

    def test_INVERT(self):
        INVERT_port = neur.Neuron(weights=[-1], bias=0.5)
        self.INVERT_port = INVERT_port
        tests = [[0], [1]]
        target = [1, 0]
        print("Invert:")
        self.neuronTester(tests, target, INVERT_port)

    def test_ManualAdjusted_INVERT(self):
        INVERT_port = neur.Neuron(weights=[-100], bias=10)
        self.INVERT_port = INVERT_port
        tests = [[0], [1]]
        target = [1, 0]
        print("Adj Invert:")

        self.neuronTester(tests, target, INVERT_port)


    def test_AND(self):
        AND_port = neur.Neuron(weights=[0.5, 0.5], bias=-1)
        self.AND_port = AND_port
        tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
        target = [0, 0, 0, 1]
        print("AND:")
        self.neuronTester(tests, target, AND_port)

    def test_ManualAdjusted_AND(self):
        AND_port = neur.Neuron(weights=[4.5, 4.5], bias=-7.5)
        self.AND_port = AND_port
        tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
        target = [0, 0, 0, 1]
        print("Adj AND:")
        # for n in range(10000):
        self.neuronTester(tests, target, AND_port)

    def test_OR(self):
        OR_port = neur.Neuron(weights=[0.5, 0.5], bias=-0.5)
        self.OR_port = OR_port
        tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
        target = [0, 1, 1, 1]
        print("OR:")
        self.neuronTester(tests, target, OR_port)

    def test_ManualAdjusted_OR(self):
        OR_port = neur.Neuron(weights=[4, 4], bias=-2)
        self.OR_port = OR_port
        tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
        target = [0, 1, 1, 1]
        print("Adj OR:")
        self.neuronTester(tests, target, OR_port)

    def test_NOR(self):
        NOR_port = neur.Neuron(weights=[-0.5, -0.5], bias=0)
        self.NOR_port = NOR_port
        tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
        target = [1, 0, 0, 0]
        print("NOR:")
        self.neuronTester(tests, target, NOR_port)

    def test_ManualAdjusted_NOR(self):
        NOR_port = neur.Neuron(weights=[-4, -4], bias=2)
        self.NOR_port = NOR_port
        tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
        target = [1, 0, 0, 0]
        print("Adj NOR:")
        self.neuronTester(tests, target, NOR_port)

    def test_party(self):
        Party_port = neur.Neuron(weights=[0.6, 0.3, 0.2], bias=-0.4)
        self.Party_port = Party_port
        tests = [[0, 0, 0 ], [0, 1, 0], [1, 0, 0], [1, 1,0], [0, 0, 1 ], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
        target = [0, 0, 1, 1, 0, 1, 1, 1]
        print("Party:")
        self.neuronTester(tests, target, Party_port)

    def test_ManualAdjusted_party(self):
        Party_port = neur.Neuron(weights=[4, 2, 2], bias=-3)
        self.Party_port = Party_port
        tests = [[0, 0, 0 ], [0, 1, 0], [1, 0, 0], [1, 1,0], [0, 0, 1 ], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
        target = [0, 0, 1, 1, 0, 1, 1, 1]
        print("Adj Party:")
        self.neuronTester(tests, target, Party_port)

    def test_NAND(self):
        NAND_port = neur.Neuron(weights=[-0.5, -0.5], bias=0.5)
        self.NAND_port = NAND_port
        tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
        target = [1, 1, 1, 0]
        print("NAND:")
        self.neuronTester(tests, target, NAND_port)

    def test_ManualAdjusted_NAND(self):
        NAND_port = neur.Neuron(weights=[-2.5, -2.5], bias=4.5)
        self.NAND_port = NAND_port
        tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
        target = [1, 1, 1, 0]
        print("Adj NAND:")
        self.neuronTester(tests, target, NAND_port)


    def test_halfAdder(self):
        print('Half Adder Port:')
        half_Adder = neurNet.NeuronNetwork([["OR_port", "NAND_port", "AND"], ["AND_port", "AND_port"]])
        half_Adder.set_network_weights(    [[ [4.0, 4.0]  ,[-2.5, -2.5], [4.5, 4.5]], [[4.5, 4.5, 4.5,], [-2.5, -2.5, -2.5] ]])
        half_Adder.set_network_bias([[-2, 4.5, -7.5], [-7.5, -2]])
        tests = [[0, 0], [0, 1], [1, 0], [1, 1]]
        target = [[0, 0], [0,1], [0,1], [1,0]]
        self.networkTester(tests, target, half_Adder)
