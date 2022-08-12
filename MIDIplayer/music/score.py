from enum import Enum

#
#		IDENTIFIES THE TYPE OF NOTATION
#


class NotationType(Enum):
    NOTE = 1
    CHORD = 2

#
#		A NOTATION OBJECT CONTAINS THE NoTE'S/CHORD'S ATTRIBUTES
#

class Notation:

    def __init__(self, type, key, duration, octave, velocity):
        self.type = type
        self.key = key
        self.velocity = velocity
        self.octave = octave
        self.duration = duration

    def get_type(self):
        return self.type

    def get_key(self):
        return self.key
        
    def get_velocity(self):
        return self.velocity

    def get_octave(self):
        return self.octave

    def get_duration(self):
        return self.duration

#
#		A SCORE CONTAINS MULTIPLES INSTRUMENTS, EACH WITH ITS OWN NOTATIONS
#

class Score(object):

    def __init__(self, instruments_count, res):
        self.instrument = dict()
        self.instrument_count = instruments_count
        self.res = res
        self.duration = 0
        for i in range(instruments_count):
            self.instrument[i] = dict()  

#		THE NOTATION IS ADDED IN A DICTIONARY WHOSE KEYS ARE RELATIVE POSITIONS IN THE SCORE

    def add_notation(self, insIdx, pos, notation):
        ins = self.instrument[insIdx]
        relpos = round(pos/self.res)
        self.duration = max(self.duration, relpos + 1)  

        if relpos in ins:
            ins[relpos].append(notation)
        else:
            ins[relpos] = [notation]    

    def get_notations_in_relpos(self, insIdx, relpos):
        ins = self.instrument[insIdx]

        if relpos in ins:
            return ins[relpos]
        else:
            return None

    def get_instrument_count(self):
        return self.instrument_count
    
    def get_instrument(self, idx):
        return self.instrument[idx]

    def get_res(self):
        return self.res
      
    def get_duration(self):
        return self.duration