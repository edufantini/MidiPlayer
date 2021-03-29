import networkx as nx
import matplotlib.pyplot as plt
import MIDIplayer
import rich
from MIDIplayer import B, Db, Eb

player = MIDIplayer.Player(name="redbone", bpm=81, to_port=True)

Ebm = MIDIplayer.Chord(Eb, "minor")

for i in range(0, 2):

	player.log("{}".format(i))

	player.play_chord(MIDIplayer.Chord(B), 2, 64, 2)
	player.play_chord(MIDIplayer.Chord(Db), 3, 64, 3/2)
	player.play_chord(Ebm, 3, 64, 4)

# player.play_note(B, 4, 64, 2)
# player.play_note(Db, 4, 64, 3/2)
# player.play_note(Eb, 4, 64, 9/2)

player.save_file()


# player.console.print(player.graph.out_edges(data=True))
# nx.draw_circular(G)
# plt.show()
