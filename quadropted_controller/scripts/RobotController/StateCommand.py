#!/usr/bin/env python3
# Author: lnotspotl, abutalipovvv
import numpy as np
from enum import Enum


class BehaviorState(Enum):
    REST = 0
    TROT = 1
    CRAWL = 2
    STAND = 3


class State(object):
    def __init__(self, default_height):
        
        self.velocity = np.array([0.0, 0.0])
        self.yaw_rate = 0.0
        self.robot_height = -default_height

        
        self.foot_locations = np.zeros((3, 4))

        
        self.body_local_position = np.array([0.0, 0.0, 0.0])
        self.body_local_orientation = np.array([0.0, 0.0, 0.0])
        
        
        self.imu_roll = 0.0
        self.imu_pitch = 0.0
        
        
        self.ticks = 0
        self.behavior_state = BehaviorState.REST



class Command:
    def __init__(self, robot_height):
        self.robot_height = -robot_height
        self.velocity = np.array([0.0, 0.0, 0.0])      # [x, y, z]
        self.yaw_rate = np.array([0.0, 0.0, 0.0])     # [roll, pitch, yaw]
        self.rest_event = False
        self.trot_event = False
        self.crawl_event = False
        self.stand_event = False



