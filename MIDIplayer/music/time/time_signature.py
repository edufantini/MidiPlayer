import mido


class TimeSignature(object):
    def __init__(self, numerator, denominator, upbeats=None):
        if upbeats is None:
            upbeats = [1]
        if numerator is None:
            numerator = 4
        if denominator is None:
            denominator = 4

        self.numerator = numerator
        self.denominator = denominator
        self.upbeats = upbeats

        # TODO
        #   enviar mensagem de alteração de ts

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

    def get(self):
        return mido.MetaMessage("time_signature", numerator=self.numerator, denominator=self.denominator)