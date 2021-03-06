from functools import total_ordering
import math

class MinHeap:

    def __init__(self):
        self.arr_heap = [None]

    def __str__(self):
        return str(self.arr_heap[1:])

    def __repr__(self):
        return str(self)
        
    def esquerda(self, i:int) ->int:
        """
            Retorna a posição do filho a esquerda de i
        """
        return 2*i

    def direita(self, i:int) ->int:
        """
            Retorna a posição do filho a direita de i
        """
        return 2*i+1

    def pai(self, i) ->int:
        """
        Retorna a posição do pai do i-ésimo nó
        """
        return math.floor(i/2)


    @property
    def pos_ultimo_item(self):
        return len(self.arr_heap)-1
    
    
    def troca(self, pos_1, pos_2):
        aux = self.arr_heap[pos_1]
        self.arr_heap[pos_1] = self.arr_heap[pos_2]
        self.arr_heap[pos_2] = aux


    def e_uma_folha(self, posicao):
        return posicao >= len(self.arr_heap)//2 and posicao <= len(self.arr_heap)


    def refaz(self, pos_raiz_sub_arvore:int):
        pos_pai = pos_raiz_sub_arvore
        pos_menor_filho = self.esquerda(pos_pai)

        val_raiz_sub_arvore = self.arr_heap[pos_raiz_sub_arvore]

        while pos_menor_filho<=self.pos_ultimo_item:
            if pos_menor_filho<self.pos_ultimo_item:
                val_filho_direita = self.arr_heap[self.direita(pos_pai)]
                if val_filho_direita<self.arr_heap[pos_menor_filho]:
                    pos_menor_filho = self.direita(pos_pai)

            if val_raiz_sub_arvore<self.arr_heap[pos_menor_filho]:
                break
                
            self.arr_heap[pos_pai] = self.arr_heap[pos_menor_filho]

            pos_pai = pos_menor_filho
            pos_menor_filho = self.esquerda(pos_pai)

        self.arr_heap[pos_pai] = val_raiz_sub_arvore


    def insere(self,item):
        self.arr_heap.append(None)
        pos_inserir = self.pos_ultimo_item
        pai_pos_inserir = self.pai(pos_inserir)

        while pos_inserir>1 and self.arr_heap[pai_pos_inserir]>item:
            self.arr_heap[pos_inserir] = self.arr_heap[pai_pos_inserir]

            pos_inserir = self.pai(pos_inserir)
            pai_pos_inserir = self.pai(pos_inserir)

        self.arr_heap[pos_inserir] = item


    def retira_min(self):
        if len(self.arr_heap)<=1:
            raise IndexError("Heap Vazio")

        minimo = self.arr_heap[1]
        last_val = self.arr_heap.pop(-1)
        if len(self.arr_heap)>1:
            self.arr_heap[1] = last_val
            self.refaz(1)

        return minimo


    def __str__(self):
        return str(self.arr_heap)


    def __repr__(self):
        return str(self)