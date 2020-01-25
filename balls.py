"""
Manatal python Exercise 2: Randomness Test
Author: Poompatai Puntitpong
"""

import random

def random_balls():
    balls = [(i+1) for i in range(50)]
    return sorted(random.sample(balls, k=10))