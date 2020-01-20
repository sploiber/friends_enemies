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
# and remember the order: (x, y, z, w)
Q = {(0, 0): 1, (3, 3): 1, (0, 1): -2, (1, 2): 2, (2, 3): -2}

bqm = dimod.BinaryQuadraticModel.from_qubo(Q,offset=-2.0)
results = exactsolver.sample(bqm)

# print the results
for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
