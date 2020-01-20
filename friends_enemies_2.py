import dimod

# use the exact solver to find energies for all states. This is only
# realistic for very small problems.
exactsolver = dimod.ExactSolver()

# Set up the QUBO. Start with the equations from the slides:
# x + y - 2xy - 1
# - y - z + 2yz
# z + w - 2zw - 1
# ------------------
# x + w - 2xy + 2yz - 2zw - 2
Q = {('x', 'x'): 1, ('w', 'w'): 1, ('x', 'y'): -2, ('y', 'z'): 2, ('z', 'w'): -2}

bqm = dimod.BinaryQuadraticModel.from_qubo(Q,offset=-2.0)
results = exactsolver.sample(bqm)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
