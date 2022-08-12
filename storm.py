import networkx as nx
import matplotlib.pyplot as plt
import MIDIplayer
import rich
from MIDIplayer import D, E, F, C, A, G, Bb
from MIDIplayer.music.score import NotationType as nt, Score, Notation

#
#	Iniciando o Player
#

player = MIDIplayer.Player(name="song of storms", n_tracks=2, bpm=60, to_port=True)

#
#	Definindo acordes
#

c_Dm = MIDIplayer.Chord(D, "minor")
c_Em = MIDIplayer.Chord(E, "minor")
c_Bb = MIDIplayer.Chord(Bb)
c_F = MIDIplayer.Chord(F)
c_A = MIDIplayer.Chord(A)


#
#	Create score with 2 instruments and resolution = 1/6:
#

score = Score(2, 1/6)

#
#	Writes bass and chords on instrument 0:
#

score.add_notation(0, 0, Notation(nt.NOTE, D, 1, 1, 64))
score.add_notation(0, 1/3, Notation(nt.CHORD, c_Dm, 1/3, 2, 64))
score.add_notation(0, 2/3, Notation(nt.CHORD, c_Dm, 1/3, 2, 64))
score.add_notation(0, 1, Notation(nt.NOTE, E, 1, 1, 64))
score.add_notation(0, 1+1/3, Notation(nt.CHORD, c_Em, 2/3, 2, 64))

score.add_notation(0, 2+0, Notation(nt.NOTE, F, 1, 1, 64))
score.add_notation(0, 2+1/3, Notation(nt.CHORD, c_F, 1/3, 2, 64))
score.add_notation(0, 2+2/3, Notation(nt.CHORD, c_F, 1/3, 2, 64))
score.add_notation(0, 3+0, Notation(nt.NOTE, E, 1, 1, 64))
score.add_notation(0, 3+1/3, Notation(nt.CHORD, c_Em, 2/3, 2, 64))

score.add_notation(0, 4+0, Notation(nt.NOTE, Bb, 1, 1, 64))
score.add_notation(0, 4+1/3, Notation(nt.CHORD, c_Bb, 1/3, 1, 64))
score.add_notation(0, 4+2/3, Notation(nt.CHORD, c_Bb, 1/3, 1, 64))
score.add_notation(0, 5+0, Notation(nt.NOTE, F, 1, 1, 64))
score.add_notation(0, 5+1/3, Notation(nt.CHORD, c_F, 2/3, 1, 64))

score.add_notation(0, 6+0, Notation(nt.NOTE, Bb, 1, 1, 64))
score.add_notation(0, 6+1/3, Notation(nt.CHORD, c_Bb, 1/3, 1, 64))
score.add_notation(0, 6+2/3, Notation(nt.CHORD, c_Bb, 1/3, 1, 64))
score.add_notation(0, 7+0, Notation(nt.NOTE, A, 1, 1, 64))
score.add_notation(0, 7+1/3, Notation(nt.CHORD, c_A, 2/3, 1, 64))

score.add_notation(0, 8+0, Notation(nt.NOTE, D, 1, 1, 64))
score.add_notation(0, 8+1/3, Notation(nt.CHORD, c_Dm, 1/3, 2, 64))
score.add_notation(0, 8+2/3, Notation(nt.CHORD, c_Dm, 1/3, 2, 64))
score.add_notation(0, 9+0, Notation(nt.NOTE, E, 1, 1, 64))
score.add_notation(0, 9+1/3, Notation(nt.CHORD, c_Em, 2/3, 2, 64))

score.add_notation(0, 10+0, Notation(nt.NOTE, F, 1, 1, 64))
score.add_notation(0, 10+1/3, Notation(nt.CHORD, c_F, 1/3, 2, 64))
score.add_notation(0, 10+2/3, Notation(nt.CHORD, c_F, 1/3, 2, 64))
score.add_notation(0, 11+0, Notation(nt.NOTE, E, 1, 1, 64))
score.add_notation(0, 11+1/3, Notation(nt.CHORD, c_Em, 2/3, 2, 64))

score.add_notation(0, 12+0, Notation(nt.NOTE, Bb, 1, 1, 64))
score.add_notation(0, 12+1/3, Notation(nt.CHORD, c_Bb, 1/3, 1, 64))
score.add_notation(0, 12+2/3, Notation(nt.CHORD, c_Bb, 1/3, 1, 64))
score.add_notation(0, 13+0, Notation(nt.NOTE, A, 1, 1, 64))
score.add_notation(0, 13+1/3, Notation(nt.CHORD, c_A, 2/3, 1, 64))

score.add_notation(0, 14+0, Notation(nt.NOTE, D, 1, 1, 64))
score.add_notation(0, 14+1/3, Notation(nt.CHORD, c_Dm, 1/3, 2, 64))
score.add_notation(0, 14+2/3, Notation(nt.CHORD, c_Dm, 1/3, 2, 64))
score.add_notation(0, 15+0, Notation(nt.NOTE, D, 1, 1, 64))
score.add_notation(0, 15+1/3, Notation(nt.CHORD, c_Dm, 2/3, 2, 64))

#
#	Writes melody on instrument 1:
#

score.add_notation(1, 0, Notation(nt.NOTE, D, 1/6, 3, 64))
score.add_notation(1, 1/6, Notation(nt.NOTE, F, 1/6, 3, 64))
score.add_notation(1, 2/6, Notation(nt.NOTE, D, 2/3, 4, 64))
score.add_notation(1, 1+0, Notation(nt.NOTE, D, 1/6, 3, 64))
score.add_notation(1, 1+1/6, Notation(nt.NOTE, F, 1/6, 3, 64))
score.add_notation(1, 1+2/6, Notation(nt.NOTE, D, 2/3, 4, 64))

score.add_notation(1, 2+0, Notation(nt.NOTE, E, 3/6, 4, 64))
score.add_notation(1, 2+3/6, Notation(nt.NOTE, F, 1/6, 4, 64))
score.add_notation(1, 2+4/6, Notation(nt.NOTE, E, 1/6, 4, 64))
score.add_notation(1, 2+5/6, Notation(nt.NOTE, F, 1/6, 4, 64))
score.add_notation(1, 3+0, Notation(nt.NOTE, E, 1/6, 4, 64))
score.add_notation(1, 3+1/6, Notation(nt.NOTE, C, 1/6, 4, 64))
score.add_notation(1, 3+2/6, Notation(nt.NOTE, A, 4/6, 3, 64))

score.add_notation(1, 4+0, Notation(nt.NOTE, A, 2/6, 3, 64))
score.add_notation(1, 4+2/6, Notation(nt.NOTE, D, 2/6, 3, 64))
score.add_notation(1, 4+4/6, Notation(nt.NOTE, F, 1/6, 3, 64))
score.add_notation(1, 4+5/6, Notation(nt.NOTE, G, 1/6, 3, 64))
score.add_notation(1, 5, Notation(nt.NOTE, A, 6/6, 3, 64))

score.add_notation(1, 6+0, Notation(nt.NOTE, A, 2/6, 3, 64))
score.add_notation(1, 6+2/6, Notation(nt.NOTE, D, 2/6, 3, 64))
score.add_notation(1, 6+4/6, Notation(nt.NOTE, F, 1/6, 3, 64))
score.add_notation(1, 6+5/6, Notation(nt.NOTE, G, 1/6, 3, 64))
score.add_notation(1, 7, Notation(nt.NOTE, E, 6/6, 3, 64))

score.add_notation(1, 8, Notation(nt.NOTE, D, 1/6, 3, 64))
score.add_notation(1, 8+1/6, Notation(nt.NOTE, F, 1/6, 3, 64))
score.add_notation(1, 8+2/6, Notation(nt.NOTE, D, 2/3, 4, 64))
score.add_notation(1, 9+0, Notation(nt.NOTE, D, 1/6, 3, 64))
score.add_notation(1, 9+1/6, Notation(nt.NOTE, F, 1/6, 3, 64))
score.add_notation(1, 9+2/6, Notation(nt.NOTE, D, 2/3, 4, 64))

score.add_notation(1, 10+0, Notation(nt.NOTE, E, 3/6, 4, 64))
score.add_notation(1, 10+3/6, Notation(nt.NOTE, F, 1/6, 4, 64))
score.add_notation(1, 10+4/6, Notation(nt.NOTE, E, 1/6, 4, 64))
score.add_notation(1, 10+5/6, Notation(nt.NOTE, F, 1/6, 4, 64))
score.add_notation(1, 11+0, Notation(nt.NOTE, E, 1/6, 4, 64))
score.add_notation(1, 11+1/6, Notation(nt.NOTE, C, 1/6, 4, 64))
score.add_notation(1, 11+2/6, Notation(nt.NOTE, A, 4/6, 3, 64))

score.add_notation(1, 12+0, Notation(nt.NOTE, A, 2/6, 3, 64))
score.add_notation(1, 12+2/6, Notation(nt.NOTE, D, 2/6, 3, 64))
score.add_notation(1, 12+4/6, Notation(nt.NOTE, F, 1/6, 3, 64))
score.add_notation(1, 12+5/6, Notation(nt.NOTE, G, 1/6, 3, 64))
score.add_notation(1, 13+0, Notation(nt.NOTE, A, 4/6, 3, 64))
score.add_notation(1, 13+4/6, Notation(nt.NOTE, A, 2/6, 3, 64))

score.add_notation(1, 14, Notation(nt.NOTE, D, 6/6, 3, 64))

#
#	Signs and plays the score:
#

player.play_score(score)
