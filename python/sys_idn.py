import matplotlib.pyplot as plt
import numpy as np
from sistema_desconhecido import sistema_desconhecido
import csv

class system_identification():

    def __init__(self, max_period, min_period, generate_periods):
        self.max_period = max_period
        self.min_period = min_period
        self.generate_periods = generate_periods
        self.periods = np.arange(self.max_period, self.min_period-1, -1)
        self.frequencies = 2*np.pi/self.periods

    def _one_period(self, freq):
        return np.cos(freq*np.arange(2*np.pi/freq))

    def frequencies_array(self):
        return self.frequencies

    def input_generator(self):
        x = []

        for w in self.frequencies:
            for T in np.arange(self.generate_periods):
                x = np.append(x, self._one_period(w))

        x_file = np.zeros((2,len(x)))
        x_file[0] = np.arange(len(x))
        x_file[1] = x

        np.savetxt("input.txt",
                   x_file.transpose(), delimiter=" ",
                   header="Sample Amplitude_[a.u.]")
        return x

    def output_processor(self, y, proc_period):
        position = 0
        H = []
        for N in self.periods:
            for T in np.arange(self.generate_periods):
                if(T == proc_period):
                    H = np.append(H, np.max(y[position:(position+N)]))
                position += N
        H_file = np.zeros((2,len(H)))
        H_file[0] = self.frequencies
        H_file[1] = H
        np.savetxt("frequency_response.txt",
                   H_file.transpose(), delimiter=" ",
                   header="Frequency_[rad] Amplitude_[a.u.]")
        return H

# # Input generator
# max_period = 100
# min_period = 2
# generate_periods = 100
#
# # Pos processor
# proc_period = 99

sys_idn = system_identification(100, 2, 100)
x = sys_idn.input_generator()
y = sistema_desconhecido(x)
H = sys_idn.output_processor(y, 99)

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
plt.plot(sys_idn.frequencies_array(), H)
plt.xlabel('Frequency [rad]')
plt.ylabel('Amplitude [a.u.]')
plt.grid()

plt.savefig('frequency_response.png')
plt.show()
