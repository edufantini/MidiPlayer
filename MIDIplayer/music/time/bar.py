from llist import dllist

from ..rest import Rest
from ...player.instruction import Instruction


class Bar(object):
	def __init__(self, time_signature, upbeats):

		# if none is specified, use TS as default
		if upbeats is None:
			upbeats = time_signature.upbeats

		# the target number of beats
		self.duration = time_signature.numerator

		# counter
		self.beat_count = 0

		# list of strong beats position
		self.upbeats = upbeats

		self.beats = []

		#   lista onde vão ficar as instrução
		#   de tocar chord/nota
		self.instructions = dllist()

	def __add__(self, new):

		remaining_beats = self.duration-self.beat_count

		# check if the current bar has space left
		if remaining_beats >= new.duration:

			# TODO
			#   create instance of Instruction with new
			new_inst = Instruction(new, self.beat_count)
			self.instructions.append(new_inst)

		else:

			# IDEA
			#   criar a fila de reproduzacao antes
			#   de mexer aqui, pq essa situação
			#   precisa modificar a fila adicionando
			#   outra barra

			# TODO
			#   create instance of Instruction with new
			#   and duration = new.duration - remaining.
			#   criar outra barra e adicionar o restante
			#   em uma instrução nessa nova barra

			#   colocar a nova barra na lista de reproduzir
			pass

	# TODO

	#   atualizar o campo self.beat_count
	self.beat_count = self.remaining_beats - new.duration
	return self

	# retornar uma lista de objetos mido
	def format(self):

		# if bar is not full, complete it with rest
		remaining_beats = self.duration-self.beat_count
		if remaining_beats != 0:
			# rest = Rest(remaining_beats)
			rest = Instruction(Rest(remaining_beats), self.beat_count)
			self.instructions.append(rest)

		# now we can translate it to mido objects
