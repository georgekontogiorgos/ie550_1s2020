import numpy as np

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
