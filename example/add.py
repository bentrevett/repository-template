import numpy as np


def add_1(x):
    y = np.add(x, 1)
    return y


if __name__ == "__main__":
    x = np.array([0, 1, 2])
    y = add_1(x)
    print(y)
