# Author: Skylar Payne
# This file defines a Glove object for use in the Hacktech.io entry of
# Skylar Payne, Yvonne Fung, Max Camacho, and Allen Sallinger.

import serial
import math


class Glove:
    thumbFlex = 0
    indexFlex = 0
    middleFlex = 0
    orientationX = 0
    orientationY = 0
    orientationZ = 0

    #Pass in the commport that the XBee is plugged into
    def __init__(self, commport):
        self.commport = commport
        self.ser = serial.Serial(commport, 9600)
        self.ser.timeout = None

    #Call this method before using any of the member data!!
    def update(self):
        self.ser.write(bytes(1))

        inputs = self.ser.read(6)

        
        self.thumbFlex = math.floor(3 * (inputs[0] - 50) / 25)
        self.middleFlex = math.floor(3 * (inputs[1] - 30) / 30)
        self.indexFlex = math.floor(3 * (inputs[2] - 30) / 25)
        
        self.orientationX = math.floor(5 * (inputs[3] - 60) / 50) - 2
        self.orientationY = math.floor(5 * (inputs[4] - 60) / 50) - 2
        self.orientationZ = math.floor(5 * (inputs[5] - 60) / 40) - 2

        
        
