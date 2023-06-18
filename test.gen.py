import numpy as np
import time
from typing import List, Dict, Tuple

from modules.cgDNAUtils import _constructSeqParms_closed

if __name__ == "__main__":


    seq = 'ATCGGTCTAGATCGAATCGGTCTAGATCGAATCGGTCTAGATCGATA'
    seq = 'ATCGCGAT'

    _DEFAULT_DATASET = 'cgDNA+_Curves_BSTJ_10mus_FS'

    _constructSeqParms_closed(seq,_DEFAULT_DATASET)