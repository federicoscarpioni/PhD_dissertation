from multisine.multisine import Multisine
import numpy as np

frequencies = [1, 10, 100, 1000] # in Hz
amplitudes = np.ones(frequencies.size) * 0.05  # in V
sampling_frequency = 10000 # in Hz