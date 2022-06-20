#
# Nomes: Ana Laura
#        Thais
#        Gabriela
#        Nicholas
#        Victor Hugo
#


from pulp import *

prob = LpProblem("Maximiza-Lucro", LpMaximize)

# Somente aceitaveis valores maiores que zero para as variaveis
x1 = LpVariable("x1", 900, 2000)
x2 = LpVariable("x2", 100, 400)
x3 = LpVariable("x3", 900, 2000)
x4 = LpVariable("x4", 500, 1200)
x5 = LpVariable("x5", 650, 1500)
x6 = LpVariable("x6", 200, 600)
x7 = LpVariable("x7", 650, 1500)

# Funcao Objetiva
prob += 0.749 * x1 + 0.5005 * x2 + 0.84 * x3 + 2.023 * x4 + 0.9275 * x5 + 0.42 * x6 + 6.8075 * x7

# Restricao de valor menor ou igual a 23 mil reais
prob += 2.14 * x1 + 1.43 * x2 + 2.4 * x3 + 5.78 * x4 + 2.65 * x5 + 1.20 * x6 + 19.45 * x7 <= 23000

# Restricao de volume menor ou igual a 14m³
prob += 0.00574 * x1 + 0.00553 * x2 + 0.00108 * x3 + 0.00174 * x4 + 0.00156 * x5 + 0.00143 * x6 + 0.0063 * x7 <= 14

# Resolucao do problema
GLPK().solve(prob)

# Imprime os valores das variaveis
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Imprime o valor de Lucro Maximo
print("Lucro Maximo = R$ {:.2f}".format(value(prob.objective)))
