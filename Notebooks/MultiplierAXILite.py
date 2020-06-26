import os, warnings
import numpy as np
from pynq import allocate
from pynq import Overlay, PL, MMIO
from pynq import DefaultIP, DefaultHierarchy
from pynq import Xlnk
from pynq.xlnk import ContiguousArray
from pynq.lib import DMA
from cffi import FFI


class MultiAXILiteDriver(DefaultIP):
    def __init__(self, description):
        self._MULTIPLIER_AXI_LITE_A_ADDR = 0x4
        self._MULTIPLIER_AXI_LITE_B_ADDR = 0x0
        self._MULTIPLIER_AXI_LITE_RESULT_ADDR = 0x8
        super().__init__(description=description)
        
    bindto = ['User_Company:SysGen:mult_lite:1.0']
    
    @property
    def a(self):
        return self.read(self._MULTIPLIER_AXI_LITE_A_ADDR)
        
    @a.setter
    def a(self, value):
        return self.write(self._MULTIPLIER_AXI_LITE_A_ADDR, value)
    
    @property
    def b(self):
        return self.read(self._MULTIPLIER_AXI_LITE_B_ADDR)
        
    @b.setter
    def b(self, value):
        return self.write(self._MULTIPLIER_AXI_LITE_B_ADDR, value)
    
    @property
    def result(self):
        return self.read(self._MULTIPLIER_AXI_LITE_RESULT_ADDR)
        
    @result.setter
    def result(self, value):
        return self.write(self._MULTIPLIER_AXI_LITE_RESULT_ADDR, value)