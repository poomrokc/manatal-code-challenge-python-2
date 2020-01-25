"""
Tests for random_balls function
Author: Poompatai Puntitpong
"""

import balls

"""
There are 10272278170 ways to select 10 items from 50 items
So there is less than 0.001% to get duplicate entries in 2000 selection
"""
def test_duplicate():
    previous_result = []
    for i in range(2000):
        this_result = balls.random_balls()
        for result in previous_result:
            assert result != this_result
        previous_result.append(this_result)

def test_duplicate2():
    previous_result = []
    for i in range(2000):
        this_result = balls.random_balls()
        for result in previous_result:
            assert result != this_result
        previous_result.append(this_result)

"""
If the selection spreads equally, each ball should be selected around 400 times in 2000 selections
So the difference between the most selected ball and the least selected ball must not be too large
I take 100 as the acceptable number
"""
def test_uniform():
    counter=[0 for i in range(50)]
    for i in range(2000):
        result = balls.random_balls()
        for ball in result:
            counter[ball-1] += 1
    assert max(counter) - min(counter) <= 100

def test_uniform2():
    counter=[0 for i in range(50)]
    for i in range(2000):
        result = balls.random_balls()
        for ball in result:
            counter[ball-1] += 1
    assert max(counter) - min(counter) <= 100