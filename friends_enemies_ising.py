import dimod
from pyqubo import Spin

exactsolver = dimod.ExactSolver()

# Binary variables
x = Spin('x')
y = Spin('y')
z = Spin('z')
w = Spin('w')

# Hamiltonian
H =  - (x * y) + (y * z) - (z * w)

# Compile the model, and turn it into a QUBO object
model = H.compile()
linear, quadratic, offset = model.to_ising()
bqm = dimod.BinaryQuadraticModel.from_ising(linear, quadratic, offset=offset)

# solve the problem
results = exactsolver.sample(bqm)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
