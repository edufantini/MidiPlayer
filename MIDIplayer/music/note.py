class Note(object):
    def __init__(self, offset, note_name, labels=None):
        # TODO: offset vai servir para MODOS? ID
        # mudar de modo somente com o offset?

        # Posição da nota no grafo:
        # EX
        #       offset 0 no tom de terC = C
        #       offset 1 no tom de C = Db
        #                 ...
        #       offset 11 no tom de C = B
        if labels is None:
            labels = []

        self.offset = offset
        self.name = note_name
        # usar como identificador, lista de strings
        # Ex
        #       .setLabel("C do refrão")
        #       .setLabel("Dm variação 2")
        #
        # Usar isso pra "DEFINIR" acordes/notas e
        # depois só usar pra chamar? como um identificador mesmo
        self.labels = labels

    # util?
    # def set_labels

    # dada a nota, pegar o valor midi dela em certa oitava
    def get_midi_val(self, octave=4):
        offset = self.offset
        # if offset > 8:
        #     octave -= 1
        return 24 + octave*12 + offset


def set_relations(graph):



    graph.add_edge(notes[0],notes[1], relation="2m")
    graph.add_edge(notes[1],notes[2], relation="2m")
    graph.add_edge(notes[2],notes[3], relation="2m"),
    graph.add_edge(notes[3],notes[4], relation="2m"), graph.add_edge(notes[4],notes[5], relation="2m"),
    graph.add_edge(notes[5],notes[6], relation="2m"),
    graph.add_edge(notes[6],notes[7], relation="2m"), graph.add_edge(notes[7],notes[8], relation="2m"),
    graph.add_edge(notes[8],notes[9], relation="2m"),
    graph.add_edge(notes[9],notes[10], relation="2m"), graph.add_edge(notes[10],notes[11], relation="2m"),
    graph.add_edge(notes[11],notes[0], relation="2m"),
    graph.add_edge(notes[0],notes[2], relation="2M"), graph.add_edge(notes[1],notes[3], relation="2M"),
    graph.add_edge(notes[2],notes[4], relation="2M"),
    graph.add_edge(notes[3],notes[5], relation="2M"), graph.add_edge(notes[4],notes[6], relation="2M"),
    graph.add_edge(notes[5],notes[7], relation="2M"),
    graph.add_edge(notes[6],notes[8], relation="2M"), graph.add_edge(notes[7],notes[9], relation="2M"),
    graph.add_edge(notes[8],notes[10], relation="2M"),
    graph.add_edge(notes[9],notes[11], relation="2M"), graph.add_edge(notes[10],notes[0], relation="2M"),
    graph.add_edge(notes[11],notes[1], relation="2M"),
    graph.add_edge(notes[0],notes[3], relation="3m"), graph.add_edge(notes[1],notes[4], relation="3m"),
    graph.add_edge(notes[2],notes[5], relation="3m"),
    graph.add_edge(notes[3],notes[6], relation="3m"), graph.add_edge(notes[4],notes[7], relation="3m"),
    graph.add_edge(notes[5],notes[8], relation="3m"),
    graph.add_edge(notes[6],notes[9], relation="3m"), graph.add_edge(notes[7],notes[10], relation="3m"),
    graph.add_edge(notes[8],notes[11], relation="3m"),
    graph.add_edge(notes[9],notes[0], relation="3m"), graph.add_edge(notes[10],notes[1], relation="3m"),
    graph.add_edge(notes[11],notes[2], relation="3m"),
    graph.add_edge(notes[0],notes[4], relation="3M"), graph.add_edge(notes[1],notes[5], relation="3M"),
    graph.add_edge(notes[2],notes[6], relation="3M"),
    graph.add_edge(notes[3],notes[7], relation="3M"), graph.add_edge(notes[4],notes[8], relation="3M"),
    graph.add_edge(notes[5],notes[9], relation="3M"),
    graph.add_edge(notes[6],notes[10], relation="3M"), graph.add_edge(notes[7],notes[11], relation="3M"),
    graph.add_edge(notes[8],notes[0], relation="3M"),
    graph.add_edge(notes[9],notes[1], relation="3M"), graph.add_edge(notes[10],notes[2], relation="3M"),
    graph.add_edge(notes[11],notes[3], relation="3M"),
    graph.add_edge(notes[0],notes[5], relation="4"), graph.add_edge(notes[1],notes[6], relation="4"),
    graph.add_edge(notes[2],notes[7], relation="4"),
    graph.add_edge(notes[3],notes[8], relation="4"), graph.add_edge(notes[4],notes[9], relation="4"),
    graph.add_edge(notes[5],notes[10], relation="4"),
    graph.add_edge(notes[6],notes[11], relation="4"), graph.add_edge(notes[7],notes[0], relation="4"),
    graph.add_edge(notes[8],notes[1], relation="4"),
    graph.add_edge(notes[9],notes[2], relation="4"), graph.add_edge(notes[10],notes[3], relation="4"),
    graph.add_edge(notes[11],notes[4], relation="4"),
    graph.add_edge(notes[0],notes[6], relation="T"), graph.add_edge(notes[1],notes[7], relation="T"),
    graph.add_edge(notes[2],notes[8], relation="T"),
    graph.add_edge(notes[3],notes[9], relation="T"), graph.add_edge(notes[4],notes[10], relation="T"),
    graph.add_edge(notes[5],notes[11], relation="T"),
    graph.add_edge(notes[6],notes[0], relation="T"), graph.add_edge(notes[7],notes[1], relation="T"),
    graph.add_edge(notes[8],notes[2], relation="T"),
    graph.add_edge(notes[9],notes[3], relation="T"), graph.add_edge(notes[10],notes[4], relation="T"),
    graph.add_edge(notes[11],notes[5], relation="T"),
    graph.add_edge(notes[0],notes[7], relation="5"), graph.add_edge(notes[1],notes[8], relation="5"),
    graph.add_edge(notes[2],notes[9], relation="5"),
    graph.add_edge(notes[3],notes[10], relation="5"), graph.add_edge(notes[4],notes[11], relation="5"),
    graph.add_edge(notes[5],notes[0], relation="5"),
    graph.add_edge(notes[6],notes[1], relation="5"), graph.add_edge(notes[7],notes[2], relation="5"),
    graph.add_edge(notes[8],notes[3], relation="5"),
    graph.add_edge(notes[9],notes[4], relation="5"), graph.add_edge(notes[10],notes[5], relation="5"),
    graph.add_edge(notes[11],notes[6], relation="5"),
    graph.add_edge(notes[0],notes[8], relation="6m"), graph.add_edge(notes[1],notes[9], relation="6m"),
    graph.add_edge(notes[2],notes[10], relation="6m"),
    graph.add_edge(notes[3],notes[11], relation="6m"), graph.add_edge(notes[4],notes[0], relation="6m"),
    graph.add_edge(notes[5],notes[1], relation="6m"),
    graph.add_edge(notes[6],notes[2], relation="6m"), graph.add_edge(notes[7],notes[3], relation="6m"),
    graph.add_edge(notes[8],notes[4], relation="6m"),
    graph.add_edge(notes[9],notes[5], relation="6m"), graph.add_edge(notes[10],notes[6], relation="6m"),
    graph.add_edge(notes[11],notes[7], relation="6m"),
    graph.add_edge(notes[0],notes[9], relation="6M"), graph.add_edge(notes[1],notes[10], relation="6M"),
    graph.add_edge(notes[2],notes[11], relation="6M"),
    graph.add_edge(notes[3],notes[0], relation="6M"), graph.add_edge(notes[4],notes[1], relation="6M"),
    graph.add_edge(notes[5],notes[2], relation="6M"),
    graph.add_edge(notes[6],notes[3], relation="6M"), graph.add_edge(notes[7],notes[4], relation="6M"),
    graph.add_edge(notes[8],notes[5], relation="6M"),
    graph.add_edge(notes[9],notes[6], relation="6M"), graph.add_edge(notes[10],notes[7], relation="6M"),
    graph.add_edge(notes[11],notes[8], relation="6M"),
    graph.add_edge(notes[0],notes[10], relation="7m"), graph.add_edge(notes[1],notes[11], relation="7m"),
    graph.add_edge(notes[2],notes[0], relation="7m"),
    graph.add_edge(notes[3],notes[1], relation="7m"), graph.add_edge(notes[4],notes[2], relation="7m"),
    graph.add_edge(notes[5],notes[3], relation="7m"),
    graph.add_edge(notes[6],notes[4], relation="7m"), graph.add_edge(notes[7],notes[5], relation="7m"),
    graph.add_edge(notes[8],notes[6], relation="7m"),
    graph.add_edge(notes[9],notes[7], relation="7m"), graph.add_edge(notes[10],notes[8], relation="7m"),
    graph.add_edge(notes[11],notes[9], relation="7m"),
    graph.add_edge(notes[0],notes[11], relation="7M"), graph.add_edge(notes[1],notes[0], relation="7M"),
    graph.add_edge(notes[2],notes[1], relation="7M"),
    graph.add_edge(notes[3],notes[2], relation="7M"), graph.add_edge(notes[4],notes[3], relation="7M"),
    graph.add_edge(notes[5],notes[4], relation="7M"),
    graph.add_edge(notes[6],notes[5], relation="7M"), graph.add_edge(notes[7],notes[6], relation="7M"),
    graph.add_edge(notes[8],notes[7], relation="7M"),
    graph.add_edge(notes[9],notes[8], relation="7M"), graph.add_edge(notes[10],notes[9], relation="7M"),
    graph.add_edge(notes[11],notes[10], relation="7M")


C = Note(0, "C")
Db = Note(1, "Db")
D = Note(2, "D")
Eb = Note(3, "Eb")
E = Note(4, "E")
F = Note(5, "F")
Gb = Note(6, "Gb")
G = Note(7, "G")
Ab = Note(8, "Ab")
A = Note(9, "A")
Bb = Note(10, "Bb")
B = Note(11, "B")
notes = [C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B]
