deischannel = DEISchannel(
    potentiostat = channel1,
    pico = pico,
    awg = multisine_gen,
    frequencies=frequencies,
)
deischannel.conditions.extend(cccv_software_conditions)

deischannel.start()