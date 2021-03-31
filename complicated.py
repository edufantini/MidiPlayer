import networkx as nx
import matplotlib.pyplot as plt
import MIDIplayer
import rich
from MIDIplayer import A, G, F

player = MIDIplayer.Player(name="complicated by mac miller", bpm=75, to_port=True)

Am7 = MIDIplayer.Chord(A, "minor7")
Gm7 = MIDIplayer.Chord(G, "minor7")
Fmaj7 = MIDIplayer.Chord(F, "major7")

for i in range(1, 3):

	# FIRST BAR
	player.play_note(A, 2, 64, 1/4)
	player.play_chord(Am7, 3, 84, 1/4)
	player.play_rest(1/2)
	player.play_chord(Am7, 3, 84, 1/4)
	player.play_rest(1/2)

	player.play_note(G, 2, 64, 1/4)
	player.play_chord(Gm7, 3, 84, 1/4)
	player.play_rest(1/4)
	player.play_chord(Gm7, 3, 84, 1/4)
	player.play_rest(3/2)


	# SENCOND BAR
	player.play_note(F, 2, 64, 1/4)
	player.play_chord(Fmaj7, 3, 84, 1/4)
	player.play_rest(1/2)
	player.play_chord(Fmaj7, 3, 84, 1/4)
	player.play_rest(1/2)


	if(i == 1):

		# SECOND BAR FIRST VARIATION
		player.play_note(G, 2, 64, 1/4)
		player.play_chord(Gm7, 3, 84, 1/4)
		player.play_rest(1/4)
		player.play_chord(Gm7, 3, 84, 1/4)
		player.play_rest(3/2)

	else:

		# SECOND BAR SECOND VARIATION
		player.play_rest(1/4)
		player.play_note(F, 2, 64, 1/4)
		player.play_chord(Fmaj7, 3, 84, 1/4)
		player.play_rest(1/2)
		player.play_chord(Fmaj7, 3, 84, 1/4)
		player.play_rest(1/2)


player.save_file()
