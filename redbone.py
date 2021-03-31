import networkx as nx
import matplotlib.pyplot as plt
import MIDIplayer
import rich
from MIDIplayer import B, Db, Eb

#
#	Iniciando o Player
#

player = MIDIplayer.Player(name="redbone by childish gambino", bpm=81, to_port=True)

#
#	Definindo acordes
#

c_B = MIDIplayer.Chord(B)
c_Db = MIDIplayer.Chord(Db)
c_Ebm = MIDIplayer.Chord(Eb, "minor")

#
#	Toca as coisa
#

for i in range(1, 3):

	player.log("{}a vez".format(str(i)))
	# play_chord(acorde, oitava, força, duração)
	player.play_chord(c_B, 2, 64, 2)
	player.play_chord(c_Db, 3, 64, 3/2)
	player.play_chord(c_Ebm, 3, 64, 4)


player.save_file()
