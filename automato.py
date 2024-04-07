q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
sigma = {'L', 'E', 'M', 'C', 'S'}

initial_state = 'q0'
f = {'q4', 'q5'}

delta = {
    'q0' : {
            'M' : {'q1'},
            'L' : {'q2'}
            },
    'q1' : {
            'M' : {'q1'},
            'L' : {'q2'}
            },
    'q2' : {
            'M' : {'q1'},
            'E' : {'q3'}
            },
    'q3' : {
            'E' : {'q3'},
            'C' : {'q4'},
            },
    'q4' : {
            'S' : {'q5'},
            }
}

from automathon import NFA

automata = NFA(q, sigma, delta, initial_state, f)

print(automata.is_valid())

print(automata.accept("LEC"))
print(automata.accept("MLEC"))
print(automata.accept("MLEC"))
print(automata.accept("MEC"))
print(automata.accept("LM"))

automata.view(
    file_name="afn_maquina_de_lavar",
    node_attr={'fontsize': '20'},
    edge_attr={'fontsize': '20pt'}
)
