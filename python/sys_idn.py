import matplotlib.pyplot as plt
import numpy as np
from sistema_desconhecido import sistema_desconhecido



# Input generator
max_period = 100
min_period = 2
generate_periods = 100

# Pos processor
proc_period = 99

def one_period(freq):
    return np.cos(freq*np.arange(2*np.pi/freq))

periods = np.arange(max_period, min_period-1, -1)
frequencies = 2*np.pi/periods

x = []

for w in frequencies:
    for T in np.arange(generate_periods):
        x = np.append(x, one_period(w))

y = sistema_desconhecido(x)

position = 0
H = []

for N in periods:
    for T in np.arange(generate_periods):
        if(T == proc_period):
            H = np.append(H, np.max(y[position:(position+N)]))
        position += N

y = sistema_desconhecido(x)

plt.subplot(3, 1, 1)
plt.stem(x, use_line_collection=True, basefmt=" ")
plt.title('Input/output graphs')
plt.ylabel('Input [a.u.]')
plt.xlabel('Time [samples]')
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(y, use_line_collection=True, basefmt=" ")
plt.ylabel('Output [a.u.]')
plt.xlabel('Time [samples]')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(frequencies, H)
plt.xlabel('Frequency [rad]')
plt.ylabel('Amplitude [a.u.]')
plt.grid()

plt.show()
