import networkx as nx
from .note import notes, set_relations


def build_graph():
	relations = nx.DiGraph()

	for note in notes:
		relations.add_node(note)

	# nesse ponto notes sai do FOR como uma lista de NoteData
	set_relations(relations)
	# print(relations.edges(data=True))
	relations.name = "Musical Relations"
	# relations.graph['graph'] = {'shape': 'circle'}
	# relations.graph['node'] = {'shape': 'circle'}
	# relations.graph['edges'] = {'arrowsize': '2.0'}
	return relations


class Music(object):
	def __init__(self):
		# plotting info
		# self.fig = plt.figure()
		# self.ax = self.fig.add_subplot(111, projection='3d')

		# the graph itself
		self.relations = build_graph()
		self.notes = self.relations.nodes
		self.degrees = self.relations.out_edges

	# TODO:
	#   helpers para informações, exp:
	#   def get_note_relations(input_note)

	# tendo uma nota e um grau (relação, etc)
	# buscar qual aresta parte de NOTA com a
	# relação DEGREE e retornar o node de chegada
	def degree2note(self, input_note, degree):
		# u: nosso nodo
		# v: lista de nodos vizinhos
		# data: arestas que nós vamos analisar
		for u, v, data in self.relations.out_edges(data=True):
			# print(u.name, v.name, data)
			if u.name == input_note.name:
				if data['relation'] == degree:
					return v
