import os, warnings
import numpy as np
from pynq import allocate
from pynq import Overlay, PL, MMIO
from pynq import DefaultIP, DefaultHierarchy
from pynq import Xlnk
from pynq.xlnk import ContiguousArray
from pynq.lib import DMA
from cffi import FFI


class FilterBankDriver(DefaultIP):
    def __init__(self, description):
        self._FILTER_BANK_PROCESS_KEY_ADDR = 0x0
        super().__init__(description=description)
        
    bindto = ['User_Company:SysGen:filter_bank:1.0']
    
    @property
    def status(self):
        return self.read(self._FILTER_BANK_PROCESS_KEY_ADDR)
        
    @status.setter
    def status(self, value):
        return self.write(self._FILTER_BANK_PROCESS_KEY_ADDR, value)

    
class StreamFilterDriver(DefaultHierarchy):
    def __init__(self, description):
        super().__init__(description)
        
    def stream_filter(self, in_buffer, out_buffer, key):
            self.filter_bank.constant = key
            self.dma_filter_bank.sendchannel.transfer(in_buffer)
            self.dma_filter_bank.sendchannel.wait()
            self.dma_filter_bank.recvchannel.transfer(out_buffer)
            self.dma_filter_bank.recvchannel.wait()
            return None

    @staticmethod
    def checkhierarchy(description):
        if 'dma_filter_bank' in description['ip'] and 'filter_bank' in description['ip']:
            return True
        return False