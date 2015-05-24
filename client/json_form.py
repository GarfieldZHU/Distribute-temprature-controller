#coding=utf-8
#__author__ = 'Garfield'

from enum import Enum
import json


class MODE(Enum):
    cold = -1
    warm = 1


class FANLEVEL(Enum):
    low = 1
    med = 2
    high = 3


class JsonForm:
    def __init__(self):
        pass