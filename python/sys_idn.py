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

        total_progress = len(self.frequencies)*self.generate_periods-1
        progress = 0

        print("Start system input generation")
        for w in self.frequencies:
            x_aux = self._one_period(w)
            for T in np.arange(self.generate_periods):
                x = np.append(x, x_aux)
                print (progress,"\t"," of ", total_progress, end="\r")
                progress += 1


        print("\nSaving input to file")

        x_file = np.zeros((2,len(x)))
        x_file[0] = np.arange(len(x))
        x_file[1] = x

        np.savetxt("input.txt",
                   x_file.transpose(), delimiter=" ",
                   header="Sample Amplitude_[a.u.]")

        print("Finish")

        return x

    def output_processor(self, y, proc_period):
        position = 100
        H = []

        print("Start output processing")

        total_progress = len(self.periods)*self.generate_periods-1
        progress = 0

        for N in self.periods:
            for T in np.arange(self.generate_periods):
                if(T == proc_period):
                    print(position, position+N)
                    H = np.append(H, np.max(y[position:(position+N)]))
                position += N
                #print (progress,"\t"," of ", total_progress, end="\r")
                #progress += 1

        print("\nSaving frequency response to file")

        H_file = np.zeros((2,len(H)))
        H_file[0] = self.frequencies
        H_file[1] = H

        np.savetxt("frequency_response.txt",
                   H_file.transpose(), delimiter=" ",
                   header="Frequency_[rad] Amplitude_[a.u.]")

        print("Finish")
        return H
