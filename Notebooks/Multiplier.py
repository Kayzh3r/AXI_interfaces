import os, warnings
import numpy as np
from pynq import allocate
from pynq import Overlay, PL, MMIO
from pynq import DefaultIP, DefaultHierarchy
from pynq import Xlnk
from pynq.xlnk import ContiguousArray
from pynq.lib import DMA
from cffi import FFI


class MultiplierDriver(DefaultIP):
    def __init__(self, description):
        self._MULTIPLIER_CONSTANT_ADDR = 0x0
        super().__init__(description=description)

    bindto = ['User_Company:SysGen:multiplier:1.0']

    @property
    def constant(self):
        return self.read(self._MULTIPLIER_CONSTANT_ADDR)

    @constant.setter
    def constant(self, value):
        self.write(self._MULTIPLIER_CONSTANT_ADDR, value)


class StreamMultiplierDriver(DefaultHierarchy):
    def __init__(self, description):
        super().__init__(description)

    def stream_multiply(self, in_buffer, out_buffer, constant):
            self.multiplier.constant = constant
            self.dma_multiplier.sendchannel.transfer(in_buffer)
            self.dma_multiplier.sendchannel.wait()
            self.dma_multiplier.recvchannel.transfer(out_buffer)
            self.dma_multiplier.recvchannel.wait()
            return None
        
    @staticmethod
    def checkhierarchy(description):
        if 'dma_multiplier' in description['ip'] and 'multiplier' in description['ip']:
            return True
        return False