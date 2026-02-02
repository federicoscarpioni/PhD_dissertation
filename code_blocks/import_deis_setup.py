from pathlib import Path
import json
import numpy as np

from pyeclab import BiologicDevice, ChannelConfig, FileWriter, Channel, BANDWIDTH, E_RANGE, I_RANGE
from pyeclab.techniques import ChronoPotentiometry, generate_xctr_param
from trueformawg import TrueFormAWG, import_awg_txt
from pypicostreaming import Picoscope5000a
from deistools.processing import MultiFrequencyAnalysis, fermi_dirac_filter, BlockCalculator
from deistools.acquisition import DEISchannel, PicoCalculator, MultisineGenerator, MultisineGeneratorCombined