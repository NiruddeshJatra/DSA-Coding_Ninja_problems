from sys import *
from collections import *
from math import *

def occursOnce(a, n):
    temp = 0
    for num in a:
        temp ^= num
    
    return temp
