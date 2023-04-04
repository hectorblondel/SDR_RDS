"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
   

    def work(self, input_items, output_items):
        """example: multiply with constant"""
            
        code_differentiel = np.array([ (np.sign(x)+1)/2. for x in input_items[0]])
        
        #code_non_differentiel = np.abs(code_differentiel[1:] - code_differentiel[:-1])
        
        
        output_items[0][:] =  code_differentiel 
        return len(output_items[0])
        
        
