import mido
from ..music.score import NotationType as nt
from ..music import Music
from ..music.time.time_signature import TimeSignature
from time import sleep

from rich import pretty
from rich.console import Console
from rich.text import Text
from rich.traceback import install
from rich.table import Table
from threading import Timer, Thread

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

		self.to_port = to_port

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

			table = Table(title="\n[yellow]Available output ports")
			table.add_column("#", style="green bold", justify="left")
			table.add_column("Outport name", style="white", justify="center")
			for id, port in enumerate(outs):
				table.add_row(str(id), port)

			self.console.print(table, justify="center")
			i = int(self.console.input("\t\t\t ➜ Select by output id: [yellow bold]# "))
			self.out_port = mido.open_output(outs[i])
			self.log("\n\t\t ➜ Selected out port: \n\t\t[bold green]{}[/]\n".format(self.out_port.name))

		#
		#               DONE
		#

		self.console.rule("")
		self.console.print("[bold green][✓] Player created [/]", justify="center")
		self.console.rule("")
		self.console.print("[bold] Press enter to start", justify="center")
		self.console.input()
		self.console.rule("")

	def set_time_signature(self, time_signature):
		self.time_signature = time_signature
		self.history.append(self.time_signature.get())
		self.log("\t➜ Time Signature set to {}".format(str(self.time_signature)))

	def start_msg(self, msg):
		self.out_port.send(msg)
		# self.log("\n\n\t➜ Message '{}' sent to port '{}'".format(msg, self.out_port))
		self.log("\t➜ Message '{}' sent to port".format(msg))

	def stop_msg(self, msg):
		msg.velocity = 0
		self.out_port.send(msg)
		# self.log("\n\n\t➜ Message '{}' sent to port '{}'".format(msg, self.out_port))
		self.log("\t➜ Message '{}' sent to port".format(msg))

	def play_rest(self, duration):
		dur_ticks = duration*self.resolution
		delta_t = mido.tick2second(dur_ticks, self.resolution, self.tempo)
		self.log("\t➜ Resting for {} seconds".format(str(delta_t)))
		sleep(delta_t)


	def play_note(self, note, octave, velocity, duration, now=False):

		midi_val = note.get_midi_val(octave)
		dur_ticks = duration*self.resolution
		delta_t = mido.tick2second(dur_ticks, self.resolution, self.tempo)
		msg = mido.Message('note_on', velocity=velocity, note=midi_val)

		if self.out_port != None:
			# turn on
			self.start_msg(msg)

			if not now:
				# wait duration
				self.log("\t➜ Sleeping for {} seconds".format(str(delta_t)))
				sleep(delta_t)
				# trocar sleep por await

				# turn off
				self.stop_msg(msg)
			else:
				Timer(delta_t, self.stop_msg, (msg,)).start()


		self.history.append(mido.Message('note_on', velocity=velocity, note=midi_val))
		self.history.append(mido.Message('note_on', velocity=0, note=midi_val, time=int(dur_ticks)))

		# print(
		#     "t" + str(time) + "\t-> "
		#     + "nota " + str(note.name) + str(octave)
		#     + ": " + str(midival)
		# )

	def play_chord(self, chord, octave, velocity, duration=4, now=False):

		curr_note = chord.root
		intervals = chord.intervals

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
		delta_t = mido.tick2second(dur_ticks, self.resolution, self.tempo)

		#
		#		PLAY CHORD NOTES
		#

		for val in midi_list:

			msg = mido.Message('note_on', velocity=velocity, note=val)
			self.history.append(msg)
			# self.log("\t➜ Message '{}' added to history".format(msg))

			if self.out_port != None:
				self.start_msg(msg)


		#
		#		WAIT CHORD DURATION
		#

		if not now:
			self.log("\t➜ Sleeping for {} seconds\n".format(str(delta_t)))
			sleep(delta_t)

		#
		#		STOP CHORD NOTES
		#

		for val in midi_list:
			msg = mido.Message('note_on', velocity=velocity, note=val)
			self.history.append(mido.Message('note_on', velocity=0, note=val, time=int(dur_ticks)))

			if self.out_port != None:
				if not now:
					self.stop_msg(msg)
				else:
					Timer(delta_t, self.stop_msg, (msg,)).start()

	
	def play_score(self, score):
		relpos = 0
		# go through all positions 
		while (relpos < score.get_duration()):
			# go through all instruments 
			for i in range(score.get_instrument_count()):
				notations = score.get_notations_in_relpos(i, relpos)

				if notations != None:
					# go through all notations 
					for notation in notations:

						key = notation.get_key()
						octave = notation.get_octave()
						velocity = notation.get_velocity()
						duration = notation.get_duration()

						# play notes in that notation
						if notation.get_type() == nt.NOTE:
							self.play_note(key, octave, velocity, duration, True)
						elif notation.get_type() == nt.CHORD:
							self.play_chord(key, octave, velocity, duration, True)							

			# advance in the score
			relpos += 1
			self.play_rest(score.get_res())
			
		
	def save_file(self):

		self.console.log(self.history)

		# for track in self.file.tracks:
		# 	for msg in self.history:
		# 		track.append(msg)
		# 		self.log("\t➜ Message '{}' added to track '{}'".format(msg, self.filename))

		self.file.save(self.filename)
		self.log("[bold green] [✓] Mid file {} saved [/bold green]".format(self.filename))
