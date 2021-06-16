from typing import List, Dict

class Vertice:
	def __init__(self, valor):
		self.valor = valor
		self.adjacencias = {}

	def insere(self, vizinho, peso:int):
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


	def e_ciclico_rec(self, vertice:Vertice, visitados:Dict[Vertice, int]) -> bool:  
		visitados[vertice.valor] = 1
  
		for vertice_adj in vertice.adjacencias.keys():
			if vertice_adj.valor not in visitados:
				if self.e_ciclico_rec(vertice_adj, visitados):
					return True
			elif visitados[vertice_adj.valor] == 1:
				return True

		visitados[vertice.valor] = 2         
		return False
    
    
	def e_ciclico(self) -> bool:
		visitados = {}
  
		for vertice in self.vertices.values():
			if vertice.valor not in visitados:
				if self.e_ciclico_rec(vertice, visitados):
					return True
 
		return False
    
    
	def e_um_dag(self) -> bool:  
		return not self.e_ciclico()
  
  
	def ordenacao_topologica(self) -> List: 
		resp = []
  
		for vertice in self.vertices.values():
			insere_por_ultimo = True
			for i, v in enumerate(resp):
				if v in vertice.adjacencias:
					resp.insert(i, vertice.valor)
					insere_por_ultimo = False
					break

			if insere_por_ultimo:
				resp.append(vertice.valor)
    
		return resp
