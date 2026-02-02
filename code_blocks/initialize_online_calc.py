frequencies = np.array(
    json.load(
        open(multisine_low_path + "waveform_metadata.json")
        )["Frequencies / Hz"]
)
frequencies = np.append(
    frequencies,
    json.load(open(multisine_high_path + "waveform_metadata.json")
              )["Frequencies / Hz"],
)
frequencies_fftshift = frequencies[20:]
sampling_time = 4e-6
time_window = 10

# Decimation
filter_cutoff = 9
filter_order = 25
time_experiment = 100
sampling_frequency = 2.5e5
resampling_frequency = 50
ds_factor = int(sampling_frequency / resampling_frequency)
buffer_size = int(time_experiment * resampling_frequency)

# Initialize the method for multi-frequency analysis
block_size =  int(time_window / sampling_time)
high_z_calculator = MultiFrequencyAnalysis(
    frequencies_fftshift, 
    np.zeros(block_size),
    np.zeros(block_size),
    sampling_time,
)
high_z_calculator.compute_freq_axis()

# Initialize the bock calculator
fermi_dirac_low_pass = fermi_dirac_filter(
    high_z_calculator.freq_axis, 
    0, 
    filter_cutoff, 
    filter_order
   )
block_calculator = BlockCalculator(
    input_size = block_size,
    sampling_time = sampling_time,
    high_z_calculator = high_z_calculator,
    lp_filter = fermi_dirac_low_pass,
    ds_factor = ds_factor,
    buffer_size =buffer_size,
)

# Inject block calculator into PicoCalculator

pico_calculator = PicoCalculator(
    pico = pico,
    block_calculator= block_calculator,
)