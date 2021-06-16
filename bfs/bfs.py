from typing import List, Dict

class Vertice:
    
	def __init__(self, valor):
		self.valor = valor
		self.adjacencias = {}

	def insere(self, vizinho:"Vertice", peso:int):
		self.adjacencias[vizinho] = peso

	def obtem_valor(self):
		return self.valor


class Grafo:
	def __init__(self):
		self.vertices = {}


	def adiciona_vertice(self, valor_vertice) -> Vertice:
     
		novo_vertice = Vertice(valor_vertice)
		self.vertices[valor_vertice] = novo_vertice
		return novo_vertice


	def adiciona_aresta(self, valor_origem, valor_destino, peso:int=1):
     
		vertice_origem = self.obtem_vertice(valor_origem)
		vertice_destino = self.obtem_vertice(valor_destino)
  
		if not vertice_origem is None and not vertice_destino is None:
			vertice_origem.insere(vertice_destino, peso)


	def obtem_vertice(self, valor_vertice) -> Vertice:
     
		if valor_vertice in self.vertices:
			return self.vertices[valor_vertice]
		else:
			return None


	def grau_separacao(self, valor_vertice_origem) -> Dict[Vertice,int]:
     
		distancia = {}
		visitou = {}
		vertice_inicial = self.obtem_vertice(valor_vertice_origem)
  
		if not vertice_inicial:
			return None
		for vertice in self.vertices.values():
			distancia[vertice] = float("inf")
			visitou[vertice] = False

		fila = []
		fila.append(vertice_inicial)
		visitou[vertice_inicial] = True
		distancia[vertice_inicial] = 0
  
		while fila:
			vertice_inicial = fila.pop(0)
			for vizinho in vertice_inicial.adjacencias.keys():
				if visitou[vizinho] == False:
					visitou[vizinho] = True
					fila.append(vizinho)
					distancia[vizinho] = distancia[vertice_inicial] + 1
                    
		return distancia