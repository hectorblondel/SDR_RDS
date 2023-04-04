"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.decim_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, t0=0, nb_ech_par_symb=8):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.decim_block.__init__(
            self,
            name='Decimation',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.complex64,np.complex64,np.complex64,np.complex64],
            decim=nb_ech_par_symb 
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.t0 = t0
        self.nb_ech_par_symb = nb_ech_par_symb

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = input_items[0][self.t0::self.nb_ech_par_symb]
        output_items[1][:] = input_items[0][self.t0+70::self.nb_ech_par_symb]
        output_items[2][:] = input_items[0][self.t0+140::self.nb_ech_par_symb]
        output_items[3][:] = input_items[0][self.t0+210::self.nb_ech_par_symb]
        return len(output_items[0])
