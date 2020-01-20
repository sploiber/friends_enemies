import dimod
from pyqubo import Binary

exactsolver = dimod.ExactSolver()

# Binary variables
x = Binary('x')
y = Binary('y')
z = Binary('z')
w = Binary('w')

# Hamiltonian
H = x + y - (2 * x * y) - 1
H += (2 * y * z) - y - z
H += z + w - (2 * z * w) - 1

# Compile the model, and turn it into a QUBO object
model = H.compile()
Q = model.to_qubo()
bqm = dimod.BinaryQuadraticModel.from_qubo(Q[0], offset=Q[1])

# solve the problem
results = exactsolver.sample(bqm)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
