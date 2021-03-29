from llist import dllistnode
from ..music import Chord, Note, Rest


class Instruction(dllistnode):
	def __init__(self, data, remaining_beats, s_beat, strong=False):
		if data is not Chord or Note or Rest:
			raise TypeError("Instruction must be of type Chord, Note or Rest.")

		super().__init__()

		# chord/rest/notes
		self.__data = data

		# starts beat
		self.s_beat = s_beat

		# IDEA
		#   quando uma instrução deve começar
		#   em uma barra e terminar em outra:
		#   * adiciona essa com e_beat = None
		#   * cria uma nova barra e adiciona
		#     uma instrução com s_beat = None
		#     e e_beat = tam_
		#	retornar uma lista com as duas

		if(data.duration > remaining_beats):
			self.e_beat = None
			self.off_set = data.duration - remaining_beats

		# end beat
		else: self.e_beat = data.duration + s_beat


	# returns the mido object
	# that corresponds to self
	def translate(self):
		# if self.
		return self.__data
