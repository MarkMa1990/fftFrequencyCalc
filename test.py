import numpy as np
import matplotlib.pyplot as plt

# fs, sample frequency
# T, sample period
fs = 1000.0
T  = 1.0/fs

# N, number of sample points 
# t, sample time
N = 1000
t = np.linspace(0, 1.0, N)

# omega_1, omega_2, the signal circular frequencies
omega_1 = 100*np.pi*2.0
omega_2 = 400*np.pi*2.0

# y, signal
y = np.cos(omega_1*t) + 0.5 * np.cos(omega_2*t + 0.2*np.pi)

# fft
fft_y = np.fft.fft(y)

# plot the signal
plt.figure(0)
plt.plot(t,y,'b-',label='signal')

# freq
# uncomment below to use the normal equation, only half of it has the right frequency
# freq = fs/N*np.linspace(0, N, N)
freq = fs/N*np.linspace(-N, N, N)/2.0

# plot the signal
plt.figure(1)
# uncomment below to use the normal equation, only half of it has the right frequency
# plt.plot(freq, np.abs((fft_y)))
plt.plot(freq, np.abs(np.fft.fftshift(fft_y)))
plt.show()
