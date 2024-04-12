from automathon import DFA

Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
sigma = {'L', 'E', 'M', 'C', 'S'}

initial_state = 'q0'
F = {'q4', 'q5'}

delta = { 'q0' : {'L' : 'q2', 'M' : 'q1'},
          'q1' : {'L' : 'q2',  'M' : 'q1'},
          'q2' : {'E' : 'q3', 'M' : 'q1'},
          'q3' : {'E' : 'q3', 'C' : 'q4', },
          'q4' : {'S' : 'q5'}
        }

automata = DFA(Q, sigma, delta, initial_state, F)
automata.is_valid()

print(automata.accept("LECS"))
print(automata.accept("MLEEC"))
print(automata.accept("LMLMMLEC"))
print(automata.accept("MEC"))
print(automata.accept("LM"))

automata.view(
    file_name="afd_maquina_de_lavar",
    node_attr={'fontsize': '20'},
    edge_attr={'fontsize': '20pt'}
)
