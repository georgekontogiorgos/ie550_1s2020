import math
import numpy as np
import matplotlib.pyplot as plt

def sistema_desconhecido(x):

    N = 400
    n = np.arange(0,N)
    hn = (1/2)*np.exp(-0.3*abs(n - 100))*np.cos(math.pi/10*n)
    y = np.convolve(hn,x)
    return y
    