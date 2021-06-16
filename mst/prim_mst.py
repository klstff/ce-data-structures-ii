from typing import List, Dict
from functools import total_ordering
from heap import MinHeap

class Vertice:
	def __init__(self, valor):
		self.valor = valor
		self.adjacencias = {}

	def insere(self, vizinho:"Vertice", peso:int):
		self.adjacencias[vizinho] = peso

	def obtem_valor(self):
		return self.valor

@total_ordering
class PesoVertice:
	def __init__(self, vertice_destino:Vertice, peso:int):
		self.vertice_destino = vertice_destino 
		self.peso = peso

	def __eq__(self, outro:"PesoVertice") ->bool:
		return self.vertice_destino.valor == outro.vertice_destino.valor and self.peso == outro.peso
	
	def __lt__(self,  outro:"PesoVertice") -> bool:
		return self.peso < outro.peso

	def __str__(self):
		return f"Peso até {self.vertice_destino.valor}: {self.peso}"
	
	def __repr__(self):
		return str(self)


class Grafo:
	def __init__(self):
		self.vertices = {}

	def adiciona_vertice(self, valor_vertice) -> Vertice:
		novo_vertice = Vertice(valor_vertice)
		self.vertices[valor_vertice] = novo_vertice
		return novo_vertice


	def adiciona_aresta(self, valor_origem, valor_destino, peso:int=1, bidirecional = False):
		vertice_origem = self.obtem_vertice(valor_origem)
		vertice_destino = self.obtem_vertice(valor_destino)
  
		if not vertice_origem is None and not vertice_destino is None:
			vertice_origem.insere(vertice_destino, peso)
			if bidirecional:
				vertice_destino.insere(vertice_origem,peso)	


	def obtem_vertice(self, valor_vertice) -> Vertice:
		if valor_vertice in self.vertices:
			return self.vertices[valor_vertice]
		else:
			return None


	def cria_arv_geradora_minima(self, valor_vertice_inicial) -> Dict[Vertice,Vertice]:
		pai = {}
		set_ja_explorado = set()
		menor_peso = {}
		vertice_inicial = self.obtem_vertice(valor_vertice_inicial)
  
		if not vertice_inicial:
			return None

		fila_min_heap = MinHeap()
  
		for vertice in self.vertices.values():
			menor_peso[vertice] = PesoVertice(vertice, float("inf"))
			pai[vertice] = None

		menor_peso[vertice_inicial].peso = 0
		fila_min_heap.insere(menor_peso[vertice_inicial])

		while len(fila_min_heap.arr_heap) > 1:
			vertice_u = fila_min_heap.retira_min().vertice_destino
			set_ja_explorado.add(vertice_u)
   
			for vertice_v in vertice_u.adjacencias.keys():
				if vertice_v not in set_ja_explorado and vertice_u.adjacencias[vertice_v] < menor_peso[vertice_v].peso:
					pai[vertice_v] = vertice_u
					menor_peso[vertice_v].peso = vertice_u.adjacencias[vertice_v]
					fila_min_heap.insere(menor_peso[vertice_v])

		return pai

