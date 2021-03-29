import mido
from ..music import Music
from ..music.time.time_signature import TimeSignature
from time import sleep

from rich import pretty
from rich.console import Console
from rich.text import Text
from rich.traceback import install
from rich.table import Table

install()
pretty.install()


class Player(object):
	def log(self, text):
		self.console.log(text)
		self.logs.append(text)

	def __init__(self, name="test", n_tracks=1, bpm=60, resolution=960, to_file=True, to_port=False):

		self.music = Music()

		self.console = Console()

		self.logs = []

		self.console.rule("[bold green] Initializing player [/]")

		# file declaration
		self.file = mido.MidiFile()

		# composing file name
		self.filename = "mid/"+name+".mid"

		self.tracks = []

		# record of all played instructions
		self.history = []

		# keep track of playing status
		self.is_playing = False

		self.resolution = resolution  # resolução ppq
		self.log("\t➜ Resolution: {} ticks/beat".format(resolution))
		self.file.ticks_per_beat = self.resolution

		# default: 4/4
		self.time_signature = None
		self.set_time_signature(TimeSignature(4, 4, upbeats=[1]))

		self.tempo = mido.bpm2tempo(bpm)
		self.log("\t➜ Tempo set to {} bpm ({} μs/beat)".format(mido.tempo2bpm(self.tempo), self.tempo))

		# appending tracks
		for i in range(1, n_tracks+1):
			track = mido.MidiTrack()
			self.tracks.append(track)
			self.file.tracks.append(self.tracks[i-1])
			self.log("\t➜ Track {} created and added to MID file".format(i-1))

		#
		#                        OUTPUT PORTS
		#
		mido.set_backend('mido.backends.rtmidi')
		self.out_port = None

		if to_port:
			outs = mido.get_output_names()

			table = Table(title="[yellow]Available output ports")
			table.add_column("#", style="green bold", justify="left")
			table.add_column("Outport name", style="white", justify="center")
			for id, port in enumerate(outs):
				table.add_row(str(id), port)

			self.console.print(table)
			i = int(self.console.input("Select by output id: [yellow bold]#"))
			self.out_port = mido.open_output(outs[i])
			self.log("\t➜ Selected out port: \n\t\t[bold green]{}[/]".format(self.out_port))

		#
		#               DONE
		#

		self.console.print("\n[bold green][✓] Player created [/]", justify="center")
		self.console.rule("")
		self.console.input("\n\n[bold] Press any key to go on... [/]")

	def set_time_signature(self, time_signature):
		self.time_signature = time_signature
		self.history.append(self.time_signature.get())
		self.log("\t➜ Time Signature set to {}".format(str(self.time_signature)))

	def start_msg(midi_val):
		msg = mido.Message('note_on', velocity=velocity, note=midi_val)
		self.out_port.send(msg)
		self.log("\t➜ Message '{}' sent to port '{}'".format(msg, self.out_port))

	def stop_msg(midi_val):
		self.out_port.send(mido.Message('note_on', velocity=0, note=midi_val))
		self.log("\t➜ Message '{}' sent to port '{}'".format(msg, self.out_port))

	def play_note(self, note, octave, velocity, duration, now=False):

		midi_val = note.get_midi_val(octave)
		dur_ticks = duration*self.resolution

		if self.out_port:
			# turn on
			start_msg(midi_val)

			if not now:
				# wait duration
				delta_t = mido.tick2second(dur_ticks, self.resolution, self.tempo)
				self.log("\t➜ Sleeping for {} seconds".format(str(delta_t)))
				sleep(delta_t)
				# trocar sleep por await

			# turn off
			stop_msg(midi_val)

		self.history.append(mido.Message('note_on', velocity=velocity, note=midi_val))
		self.history.append(mido.Message('note_on', velocity=0, note=midi_val, time=int(dur_ticks)))

		# print(
		#     "t" + str(time) + "\t-> "
		#     + "nota " + str(note.name) + str(octave)
		#     + ": " + str(midival)
		# )

	def play_chord(self, chord, octave, velocity, duration=4):
		curr_note = chord.root
		intervals = chord.intervals
		# print(intervals)

		# print(root)

		notes2play = []

		next_octave = False
		notes2play.append(curr_note)
		# caminhada pelo grafo para tocar acorde
		for interval in intervals:
			# print(interv        root = curr_noteal)
			curr_note = Music().degree2note(curr_note, interval)
			# print(curr_note)
			# print(str(curr_note.offset) + str(root.offset))
			if curr_note.offset < chord.root.offset:
				next_octave += 1
			notes2play.append(curr_note)

		# print(notes2play)

		midi_list = []

		for note in reversed(notes2play):
			if next_octave != 0:
				midi_list.append(note.get_midi_val(octave+1))
				next_octave -= 1
			else:
				midi_list.append(note.get_midi_val(octave))

		dur_ticks = duration*self.resolution

		if self.out_port:
			for val in midi_list:
				msg = mido.Message('note_on', velocity=velocity, note=val)
				self.out_port.send(msg)
				self.log("\t➜ Message '{}' sent to port '{}'".format(msg, self.out_port))

			# wait duration
			delta_t = mido.tick2second(dur_ticks, self.resolution, self.tempo)
			self.log("\t➜ Sleeping for {} seconds".format(str(delta_t)))
			sleep(delta_t)

			# turn off
			for val in midi_list:
				msg = mido.Message('note_on', velocity=0, note=val)
				self.out_port.send(msg)
				self.log("\t➜ Message '{}' sent to port '{}'".format(msg, self.out_port))

		for val in midi_list:
			msg = mido.Message('note_on', velocity=velocity, note=val)
			self.history.append(msg)
			self.log("\t➜ Message '{}' added to history".format(msg))
		for val in midi_list:
			self.history.append(mido.Message('note_on', velocity=0, note=val, time=int(dur_ticks)))

	def save_file(self):

		self.console.log(self.history)

		for track in self.file.tracks:
			for msg in self.history:
				track.append(msg)
				self.log("\t➜ Message '{}' added to track '{}'".format(msg, self.filename))

		self.file.save(self.filename)
		self.log("[bold green] [✓] Mid file {} saved [/bold green]".format(self.filename))
