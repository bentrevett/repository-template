import numpy as np


def double(x):
    y = np.multiply(x, 2)
    return y


if __name__ == "__main__":
    x = np.array([0.5, 1, 1.5])
    y = double(x)
    print(y)
