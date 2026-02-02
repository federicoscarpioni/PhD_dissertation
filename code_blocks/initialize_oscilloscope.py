pico_samples_total = 300000000
pico_capture_size = pico_samples_total
pico_sampling_time = 4
pico_sampling_time_scale = 'PS5000A_US'
pico_bandwidth_chA = 'PS5000A_5V'
pico_bandwidth_chB = 'PS5000A_500MV'
pico_current_conversion_factor = 0.01

pico = Picoscope5000a('PS5000A_DR_14BIT')
pico.set_pico(
    pico_capture_size, 
    pico_samples_total, 
    pico_sampling_time, 
    pico_sampling_time_scale, 
    saving_path,
)
pico.set_channel(
    'PS5000A_CHANNEL_A', 
    pico_bandwidth_chA,
)
pico.set_channel(
    'PS5000A_CHANNEL_B', 
    pico_bandwidth_chB, 
    pico_current_conversion_factor,
)