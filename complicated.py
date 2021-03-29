import networkx as nx
import matplotlib.pyplot as plt
import MIDIplayer
import rich
from MIDIplayer import A, G, F

player = MIDIplayer.Player(name="complicated", bpm=75, to_port=False)

Am7 = MIDIplayer.Chord(A, "minor7")
Gm7 = MIDIplayer.Chord(G, "minor7")
Fmaj7 = MIDIplayer.Chord(F, "major7")

for i in range(0, 2):

	# FIRST BAR
	player.play_note(A, 3, 64, 1)
	player.play_chord(Am7, 4, 64, 1)
	player.play_rest(1)
	player.play_chord(Am7, 4, 64, 1)

	# player.play_note(G, 3, 64, 1/2)
	# player.play_chord(Gm7, 4, 64, 1/2)
	# player.play_chord(Gm7, 4, 64, 1/2)
	# player.play_rest(1/2)
	#
	# # SENCOND BAR
	# player.play_note(F, 3, 64, 1/2)
	# player.play_chord(Fmaj7, 4, 64, 1/2)
	# player.play_rest(1/2)
	# player.play_chord(Fmaj7, 4, 64, 1/2)
	#
	# player.play_note(G, 3, 64, 1/2)
	# player.play_chord(Gm7, 4, 64, 1/2)
	# player.play_chord(Gm7, 4, 64, 1/2)
	# player.play_rest(1/2)

player.save_file()
