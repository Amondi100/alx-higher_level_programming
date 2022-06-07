#!/usr/bin/python3

def multiple_returns(sentence):
    tupp = ()
    if len(sentence) == 0:
        tupp = len(sentence), None
        return tupp
    else:
        tupp = len(sentence), sentence[0]
        return tupp
