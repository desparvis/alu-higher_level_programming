#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    maxis = float('-inf')
    bests = None
    for key, value in a_dictionary.items():
        if maxis < value:
            maxis = value
            bests = key
    return bests
