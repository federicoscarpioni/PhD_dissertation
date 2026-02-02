potentiostat_ip = "172.28.26.10"
eclabsdk_binary_path = "C:/EC-Lab Development Package/EC-Lab Development Package/"
potentiostat_channel = 1
config = ChannelConfig(
    live_plot=True,
    external_control=True,
    record_ece = False,
    record_charge = False,
)

# chrono-potentiometry technique
current = 0
duration = 102
vs_init = True
nb_steps = 0
record_dt = 1
record_dE = 5
repeat = 0
i_range = I_RANGE.I_RANGE_10mA
e_range = E_RANGE.E_RANGE_5V
bandwidth = BANDWIDTH.BW_9

device = BiologicDevice(potentiostat_ip, binary_path=eclabsdk_binary_path)
ca = ChronoAmperometry(
    device=device,
    voltage=voltage,
    duration=duration,
    vs_init=vs_init,
    nb_steps=nb_steps,
    record_dt=record_dt,
    record_dI=record_dI,
    repeat=repeat,
    e_range=e_range,
    i_range=i_range,
    bandwidth=bandwidth,
    xctr = generate_xctr_param(config),
)
ca.make_technique()
sequence = [
    ca,
]
writer = FileWriter(
    file_dir=Path(saving_directory),
    experiment_name=experiment_name,
)
channel1 = Channel(
    device,
    potentiostat_channel,
    writer=writer,
    config=config,
)
channel1.load_sequence(sequence)