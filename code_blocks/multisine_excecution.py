ms = Multisine(sampling_frequency, frequencies, amplitudes,)
ms.best_random_phases(500)
print(ms.crest_factor)
ms.normalize_waveform(1)
ms.plot('voltage')
num_period = 10
ms.fourier_analysis(num_period)
ms.plot_dft((0.001,sampling_frequency//2))