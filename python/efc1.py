import matplotlib.pyplot as plt
from sys_idn import system_identification
from sistema_desconhecido import sistema_desconhecido

## Instantiate system identification class
#   Maximum period = 100
#   Minimum period = 1
#   Periods in each frequency = 200
sys_idn = system_identification(100, 1, 200)

# Generate cosine "sweep" system input
x = sys_idn.input_generator()

# Get the system output from our input
print("Exciting system to obtain its output")
y = sistema_desconhecido(x)
print("Finish")

## Get the frequency respose
#   Eliminate first 199 periods per frequency for each frequency to eliminate transitory response
H = sys_idn.output_processor(y, 199)

## Plot all stuff ...
#   Input
print("Setting plot")
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
print("Finish")

print("Saving figure to file")
plt.savefig('frequency_response.png')
print("Finish")
plt.show()
