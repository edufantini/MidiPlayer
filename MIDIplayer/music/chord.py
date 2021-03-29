class Chord(object):

    # TODO: ao inves de receber 'type',
    # receber alguma coisa mais condizente
    # com a teoria
    def __init__(self, root, type="major"):
        self.root = root
        self.type = type
        self.intervals = self.get_intervals()

    # TODO: Função para alterar/add/rem notas do acorde
    # pq depois tem q chamar a get intervals de novo

    # TODO: tratar acordes extendidos e inversões

    def get_intervals(self):
        return {

            'major': ["3M", "3m"],
            'minor': ["3m", "3M"],
            'diminished': ["3m", "3m"],
            'augmented': ["3M", "3M"],
            'major6': ["3M", "3m", "2M"],
            'major7': ["3M", "3m", "3M"],
            'minor7': ["3m", "3M", "3m"]

        }[self.type]

    def play(self, player, octave, time, duration=4):
        player.play_chord(self, octave, time, duration)
