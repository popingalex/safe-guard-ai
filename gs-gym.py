# -*- coding: utf-8 -*-

import gym
from gym import spaces
from gym.envs.registration import register
import numpy as np

class Fire(object):
    def __init__(self, power, growth):
        self.power = power
        self.growth = growth

    def grow(self):
        self.power = self.power + self.growth

class Aircraft(object):
    def __init__(self, name, duration, fire=None):
        self.name = name
        self.duration = duration
        self.fire = fire

class TruckFleet(object):
    def __init__(self, name, count=0):
        self.name = name
        self.count = count

class FSFire(gym.Env):
    def __init__(self):
        self.aircrafts = [
            Aircraft('747-1', 10000, Fire(50, 10)),
            Aircraft('737-1', 8000, Fire(60, 8))
        ]
        self.truckFleets = [
            TruckFleet('Alpha', 4),
            TruckFleet('Bravo', 3)
        ]

        self.action_space = spaces.Tuple((
            spaces.Discrete(len(self.aircrafts)),
            *[spaces.Discrete(fleet.count) for fleet in self.truckFleets]
        ))

        self.status = [False] * len(self.aircrafts)

        print('fck')

    def step(self, action):
        return 0, 0, False, {}

    def reset(self):
        return None

class GSAgent()

register(
    id='GS-Fire-v0',
    entry_point=FSFire,
    reward_threshold=1.0,
    nondeterministic=True,
)

if __name__ == '__main__':
    env = gym.make('GS-Fire-v0')

    env.reset()
    for step in range(10):
        action = tuple((0, 1, 1))
        obs, reward, done, info = env.step(action)
        print('step {}: action {}, obs {}, reward {}, done {}, info {}'.format(step, action, obs, reward, done, info))


