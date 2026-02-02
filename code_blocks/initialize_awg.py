trueform_address = 'USB0::0x0957::0x4B07::MY59000581::0::INSTR'
waveforms_directory = 'E:/multisine_collection/'
waveform_name = '2505151210multisine_splitted_quasi-log_100kHz-10mHz_8ptd_flat_norm_random_phases'
multisine_high_path = waveforms_directory+waveform_name+'/high_band/'
multisine_high_name = 'ms_high'
multisine_low_path = waveforms_directory+waveform_name+'/low_band/'
multisine_low_name = 'ms_low'
amplitude_mulitsine = 0.1

awg_ch1 = TrueFormAWG(trueform_address, 1)
awg_ch1.clear_ch_mem()
multisine_high = import_awg_txt(multisine_high_path + "waveform.txt")
awg_ch1.load_awf(multisine_high_name, multisine_high) 
awg_ch2 = TrueFormAWG(trueform_address, 2)
awg_ch2.clear_ch_mem()
multisine_low = import_awg_txt(multisine_low_path + "waveform.txt")
awg_ch2.load_awf(multisine_low_name, multisine_low) 
awg_ch2.avalable_memory()
awg_ch1.set_offset(0)
awg_ch2.set_offset(0)
sample_rate_multisine_high = json.load(open(multisine_high_path + "waveform_metadata.json"))["Sample frequency / Hz"]
sample_rate_multisine_low = json.load(open(multisine_low_path + "waveform_metadata.json"))["Sample frequency / Hz"]
awg_ch1.set_sample_rate(sample_rate_multisine_high)
awg_ch2.set_sample_rate(sample_rate_multisine_low)
multisine_gen_high = MultisineGenerator(
    awg_ch1, 
    [waveform_name]*3,
    [0, 2, 4], 
    ['ms_high'] * 3, 
    [sample_rate_multisine_high] * 3, 
    [amplitude_galvano, amplitude_potentio, amplitude_galvano],
)
multisine_gen_low = MultisineGenerator(
    awg_ch2, 
    [waveform_name]*3,
    [0, 2, 4], 
    ['ms_low'] * 3, 
    [sample_rate_multisine_low] * 3, 
    [amplitude_galvano, amplitude_potentio, amplitude_galvano],
)
multisine_gen = MultisineGeneratorCombined(
    multisine_gen_high,
    multisine_gen_low,
    [waveform_name]*3,
)