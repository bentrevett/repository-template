import numpy as np


def subtract_1(x):
    y = np.subtract(x, 
                    1)
    return y


if __name__ == "__main__":
    x = np.array([2, 3, 4])
    y = subtract_1(x)
    print(y)
