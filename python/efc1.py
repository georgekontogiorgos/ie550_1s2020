import matplotlib.pyplot as plt
from sys_idn import system_identification
from sistema_desconhecido import sistema_desconhecido

## Instantiate system identification class
#   Maximum period = 100
#   Minimum period = 2
#   Periods in each frequency = 100
sys_idn = system_identification(100, 2, 100)

# Generate cosine "sweep" system input
x = sys_idn.input_generator()

# Get the system output from our input
y = sistema_desconhecido(x)

## Get the frequency respose
#   Eliminate first 99 periods per frequency for each frequency to eliminate transitory response
H = sys_idn.output_processor(y, 99)

## Plot all stuff ...
#   Input
plt.subplot(3, 1, 1)
plt.stem(x, use_line_collection=True, basefmt=" ")
plt.title('Input/output graphs')
plt.ylabel('Input [a.u.]')
plt.xlabel('Time [samples]')
plt.grid()

#   Output
plt.subplot(3, 1, 2)
plt.stem(y, use_line_collection=True, basefmt=" ")
plt.ylabel('Output [a.u.]')
plt.xlabel('Time [samples]')
plt.grid()

# Frequency response
plt.subplot(3, 1, 3)
plt.plot(sys_idn.frequencies_array(), H)
plt.xlabel('Frequency [rad]')
plt.ylabel('Amplitude [a.u.]')
plt.grid()

plt.savefig('frequency_response.png')
plt.show()
