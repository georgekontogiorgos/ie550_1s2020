import matplotlib.pyplot as plt
import numpy as np
from sistema_desconhecido import sistema_desconhecido

N=400;

w=0.5;

n=np.arange(0,N);

xn=np.cos(w*n);

yn=sistema_desconhecido(xn)

plt.stem(yn)
plt.show()
