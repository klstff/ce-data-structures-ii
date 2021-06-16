def setUp(moedas, troco):
    global valor_troco, conjunto_moedas, qtd_moedas, tabela
    
    valor_troco = troco
    conjunto_moedas = moedas
    qtd_moedas = len(conjunto_moedas)
    tabela = monta_tabela()

def monta_tabela():
    tabela_subproblemas = [[None for i in range(valor_troco + 1)] for i in range(qtd_moedas + 1)]    
    return tabela_subproblemas

def obtem_tabela():
    return tabela

def calcula_qtd_moedas(troco:int, pos_moeda:int=0):
    if troco == 0:
        tabela[pos_moeda][troco] = 0
        return 0
    
    elif (troco > 0 and pos_moeda == qtd_moedas) or troco < 0:
        return float("inf")
    
    else:
        com_moeda = calcula_qtd_moedas(troco - conjunto_moedas[pos_moeda], pos_moeda) + 1
        sem_moeda = calcula_qtd_moedas(troco, pos_moeda + 1)
        tabela[pos_moeda][troco] = min(com_moeda, sem_moeda)
        
    return tabela[pos_moeda][troco]