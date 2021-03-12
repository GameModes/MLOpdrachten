'''^W = N(target-output)*b'''

def test_out_weights(iteratie=None, bias=1, weights=None):
    if weights is None:
        weights = [1, 1]
    if iteratie is None:
        iteratie = [0, 0]
    print(iteratie)
    for index in range(len(iteratie)):
        print(index)
    return


def create_better_weights(learningrule=1, target=1, output=1, bias=1, iteraties=None, x_d=None):
    if x_d is None:
        x_d = [[1], [0], [0], [0], [1], [0], [0], [0], [1], [0]]
    if iteraties is None:
        iteraties = [[0, 0], [0, 1], [1, 0], [1, 1]]
    # for interatie in iteraties:
    return


learningrule = 1
iteraties = [[1, 1], [1, 0], [0, 1], [0, 0], [1, 1], [1, 0], [0, 1], [0, 0], [1, 1], [1, 0]]
XOR_d = [[0], [1], [1], [0], [0], [1], [1], [0], [0], [1]]
And_d = [[1], [0], [0], [0], [1], [0], [0], [0], [1], [0]]
firstweights = [1, 1]
bias = -1

print(iteraties)
test_out_weights(iteraties[0], bias, firstweights)