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
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32,np.float32,np.float32,np.float32,np.float32],
            decim = nb_ech_par_symb
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.t0 = t0
        self.nb_ech_par_symb = nb_ech_par_symb
 
    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = input_items[0][self.t0::self.nb_ech_par_symb]
        output_items[1][:] = input_items[0][self.t0+int(self.nb_ech_par_symb*0.25)::self.nb_ech_par_symb]
        output_items[2][:] = input_items[0][self.t0+int(self.nb_ech_par_symb*0.5)::self.nb_ech_par_symb]
        output_items[3][:] = input_items[0][self.t0+int(self.nb_ech_par_symb*0.75)::self.nb_ech_par_symb]
        
        
        imax = 0
        vmax = np.mean([x for x in output_items[0][:] if x > 0]) * np.mean([x for x in output_items[0][:] if np.real(x) <0 ])
        for i in range(1,4):
            v = np.mean([x for x in output_items[i][:] if x > 0]) * np.mean([x for x in output_items[i][:] if np.real(x) <0 ])
            if v > vmax :
                imax = i
                vmax = v
        

        output_items[4][:] = output_items[imax][:]

        #code_differentiel = np.array([ np.sign(x) for x in output_items[4][:]])
        
        #code_non_differentiel = np.abs(code_differentiel[1:] - code_differentiel[:-1])
        
        
        #output_items[5][:] =  code_differentiel
        return len(output_items[0])
