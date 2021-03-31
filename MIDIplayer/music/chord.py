class Chord(object):

    # TODO: ao inves de receber 'type',
    # receber alguma coisa mais condizente
    # com a teoria
    def __init__(self, root, type="major"):
        self.root = root
        self.type = type
        self.intervals = self.get_intervals()

    # TODO: Função para alterar/add/rem notas do acorde
    # pq depois tem q chamar a get intervals de novoz

    # TODO: tratar acordes extendidos e inversões
    # TODO: escalas, suspends

    def get_intervals(self):
        return {

            'major':            ["3M", "3m"],
            'augmented':        ["3M", "3M"],
            'major6':           ["3M", "3m", "2M"],
            'dominant7':        ["3M", "3m", "3m"],
            'major7':           ["3M", "3m", "3M"],
            'augmented7':       ["3M", "3M", "2M"],


            'minor':            ["3m", "3M"],
            'diminished':       ["3m", "3m"],
            'minor6':           ["3m", "3M", "2M"],
            'minor7':           ["3m", "3M", "3m"],
            'minor/major7':     ["3m", "3M", "3M"],
            'diminished7':      ["3m", "3m", "3m"],
            'half-diminished7':  ["3m", "3m", "3M"]

        }[self.type]

    def play(self, player, octave, time, duration=4):
        player.play_chord(self, octave, time, duration)
