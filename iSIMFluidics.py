from Fluidics import *
from Fluidics import Fluidics
# from Pumps.SyringePump import SyringePump as Pump
# from Protocols.SyringeProtocol import SyringeProtocol as Protocol
# from Valves.ViciValve import ViciValve as Valve


class iSIMFluidics(Fluidics):
    def __init__(self,gui=False):
        super().__init__()  # call __init__ method of the super class
        self.verbose = True
        Protocol = getattr(importlib.import_module('SyringeProtocol'), 'SyringeProtocol')
        Pump = getattr(importlib.import_module('SyringePump_v2'), 'SyringePump_v2')
        Valve = getattr(importlib.import_module('ViciValve'), 'ViciValve')
        self.Protocol = Protocol(gui=gui)
        self.Pump = Pump('COM14',gui=gui)
        self.Valve = Valve('COM13',gui=gui)
        self.device = self.__class__.__name__
        self.Protocol.device = self.device
        self.Pump.device = self.device
        self.Valve.device = self.device
        self.Pump.wait_factor = 1/2
        self.Pump.speed_conversion = 0.71 #1.9       0.83 / x = 3.5 / 3  -> 3.5x  = 1.8
        self.Protocol.speed = 1
        self.Protocol.closed_speed = 0.1
        self.Protocol.wait_factor = self.Pump.wait_factor
        self.Protocol.speed_conversion = self.Pump.speed_conversion
        self.Protocol.rinse_volume = 2.5

        # TBS, WBuffer, TCEP, Sample, Image Buffer, Waste
        # 2 daisy chains
        # 22 hybe solutions

        self.Valve_Commands = {
                                'Hybe21':{'valve':1, 'port':1},
                                'Hybe20':{'valve':1, 'port':2},
                                'Valve2':{'valve':1, 'port':3},
                                'Hybe22':{'valve':1, 'port':4},
                                'TCEP':{'valve':1, 'port':5},
                                'IBuffer':{'valve':1, 'port':6},
                                'M':{'valve':1, 'port':7},
                                'TBS':{'valve':1, 'port':8},
                                'WBuffer':{'valve':1, 'port':9},
                                'Waste':{'valve':1, 'port':10},


                                'Hybe11':{'valve':2, 'port':1},
                                'Hybe12':{'valve':2, 'port':2},
                                'Valve3':{'valve':2, 'port':3},
                                'Hybe13':{'valve':2, 'port':4},
                                'Hybe14':{'valve':2, 'port':5},
                                'Hybe15':{'valve':2, 'port':6},
                                'Hybe16':{'valve':2, 'port':7},
                                'Hybe17':{'valve':2, 'port':8},
                                'Hybe18':{'valve':2, 'port':9},
                                'Hybe19':{'valve':2, 'port':10},


                                'Hybe1':{'valve':3, 'port':1},
                                'Hybe2':{'valve':3, 'port':2},
                                'Hybe3':{'valve':3, 'port':3},
                                'Hybe4':{'valve':3, 'port':4},
                                'Hybe5':{'valve':3, 'port':5},
                                'Hybe6':{'valve':3, 'port':6},
                                'Hybe7':{'valve':3, 'port':7},
                                'Hybe8':{'valve':3, 'port':8},
                                'Hybe9':{'valve':3, 'port':9},
                                'Hybe10':{'valve':3, 'port':10},
                            }
        





    