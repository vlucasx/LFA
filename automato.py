from automathon import DFA

# estados
Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}

# alfabeto
sigma = {'L', 'E', 'M', 'C', 'S'}

# estado inicial
initial_state = 'q0'

# estado final
F = {'q4', 'q5'}

# tabela de transição
delta = { 'q0' : {'L' : 'q2', 'M' : 'q1'},
          'q1' : {'L' : 'q2',  'M' : 'q1'},
          'q2' : {'E' : 'q3', 'M' : 'q1'},
          'q3' : {'E' : 'q3', 'C' : 'q4', },
          'q4' : {'S' : 'q5'}
        }

# gera autômato
automata = DFA(Q, sigma, delta, initial_state, F)

# valida autômato
automata.is_valid()

# testa palavras no autômato
print(automata.accept("LECS"))
print(automata.accept("MLEEC"))
print(automata.accept("LMLMMLEC"))
print(automata.accept("MEC"))
print(automata.accept("LM"))

# visualizar autômato
automata.view(
    file_name="afd_maquina_de_lavar",
    node_attr={'fontsize': '20'},
    edge_attr={'fontsize': '20pt'}
)
