import unittest
from dfs import Grafo

class TestNode(unittest.TestCase):
    def setUp(self):
        self.arr_tests = []

        self.arr_tests.append(Grafo())
        self.arr_tests[0].adiciona_vertice(0)
        self.arr_tests[0].adiciona_vertice(1)
        self.arr_tests[0].adiciona_vertice(2)
        self.arr_tests[0].adiciona_vertice(3)
        self.arr_tests[0].adiciona_vertice(4)
        self.arr_tests[0].adiciona_vertice(5)
        self.arr_tests[0].adiciona_vertice(6)

        self.arr_tests[0].adiciona_aresta(0, 1)
        self.arr_tests[0].adiciona_aresta(1, 2)
        self.arr_tests[0].adiciona_aresta(1, 3)
        self.arr_tests[0].adiciona_aresta(2, 5)
        self.arr_tests[0].adiciona_aresta(3, 5)
        self.arr_tests[0].adiciona_aresta(4, 5)

        self.arr_tests.append(Grafo())
        self.arr_tests[1].adiciona_vertice(0)
        self.arr_tests[1].adiciona_vertice(1)
        self.arr_tests[1].adiciona_vertice(2)
        self.arr_tests[1].adiciona_vertice(3)

        self.arr_tests[1].adiciona_aresta(0, 1)
        self.arr_tests[1].adiciona_aresta(1, 2)
        self.arr_tests[1].adiciona_aresta(2, 3)
        self.arr_tests[1].adiciona_aresta(3, 1)


    def teste_e_um_dag(self):
        self.assertTrue(self.arr_tests[0].e_um_dag())
        self.assertFalse(self.arr_tests[1].e_um_dag())


    def teste_ordenacao_topologica(self):
        ordenacao = self.arr_tests[0].ordenacao_topologica()

        self.assertTrue(ordenacao.index(0) < ordenacao.index(1),f"Erro na ordenação topológica do primeiro grafo")
        self.assertTrue(ordenacao.index(1) < ordenacao.index(2),f"Erro na ordenação topológica do primeiro grafo")
        self.assertTrue(ordenacao.index(1) < ordenacao.index(3),f"Erro na ordenação topológica do primeiro grafo")
        self.assertTrue(ordenacao.index(2) < ordenacao.index(5),f"Erro na ordenação topológica do primeiro grafo")
        self.assertTrue(ordenacao.index(3) < ordenacao.index(5),f"Erro na ordenação topológica do primeiro grafo")
        self.assertTrue(ordenacao.index(4) < ordenacao.index(5),f"Erro na ordenação topológica do primeiro grafo")

class TesteDisciplinas(unittest.TestCase):
    def setUp(self):
        self.arr_testsubj = []

        self.arr_testsubj.append(Grafo())
        self.arr_testsubj[0].adiciona_vertice(0)
        self.arr_testsubj[0].adiciona_vertice(1)
        self.arr_testsubj[0].adiciona_vertice(2)
        self.arr_testsubj[0].adiciona_vertice(3)
        self.arr_testsubj[0].adiciona_vertice(4)
        self.arr_testsubj[0].adiciona_vertice(5)
        self.arr_testsubj[0].adiciona_vertice(6)

        self.arr_testsubj[0].adiciona_aresta(0, 3)
        self.arr_testsubj[0].adiciona_aresta(0, 6)
        self.arr_testsubj[0].adiciona_aresta(2, 0)
        self.arr_testsubj[0].adiciona_aresta(2, 4)
        self.arr_testsubj[0].adiciona_aresta(2, 5)
        self.arr_testsubj[0].adiciona_aresta(5, 1)

    def teste_ordenacao_topologica(self):
        ordenacao = self.arr_testsubj[0].ordenacao_topologica()
        
        arr_palavras = ["Cálculo I", "Física I", "Cálculo II", "Métodos Numéricos", "GAAV", "Física II", "Cálculo III"]
        
        print("Ordem das disciplinas:")
        for posicao in ordenacao:
            print(arr_palavras[posicao])
            

if __name__ == "__main__":
    unittest.main()
