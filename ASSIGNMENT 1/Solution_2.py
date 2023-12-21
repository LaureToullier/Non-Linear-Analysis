import numpy as np

# Nodes
nodes = np.array([
    [0.0, 0.0],
    [3.0, 4.0],
    [6.0, 0.0],
    [9.0, 4.0],
    [12.0, 0.0],
    [15.0, 4.0],
    [18.0, 0.0]
])  # m

# Restraints
rests = np.array([
    [1, 1],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [1, 1]
]).ravel()
print(rests)


# Material stiffness
E = 200e9  # GPa
A = 0.01  # m^2

elems = np.array([
    [1, 2, A, E],
    [2, 3, A, E],
    [3, 4, A, E],
    [4, 5, A, E],
    [5, 6, A, E],
    [6, 7, A, E],
    [1, 3, A, E],
    [3, 5, A, E],
    [5, 7, A, E],
    [2, 4, A, E],
    [4, 6, A, E]
])

F = np.array([
    [0, 0],
    [0, -150],
    [0, 0],
    [0, -150],
    [0, 0],
    [0, -150],
    [0, 0]
]) * 1000  # N
F = F.ravel()

n = elems.shape[0]
K_unit = np.array([
    [1, 0, -1, 0],
    [0, 0, 0, 0],
    [-1, 0, 1, 0],
    [0, 0, 0, 0]
])

k_global = []
theta = np.zeros(n)

for k in range(n):
    node_i = int(elems[k, 0] - 1)
    node_j = int(elems[k, 1] - 1)
    A = elems[k, 2]
    E = elems[k, 3]

    xy_i = nodes[node_i]
    xy_j = nodes[node_j]
    dx = xy_j[0] - xy_i[0]
    dy = xy_j[1] - xy_i[1]
    L = np.sqrt(dx**2 + dy**2)
    theta[k] = np.degrees(np.arctan2(dy, dx))
    c = np.cos(np.radians(theta[k]))
    s = np.sin(np.radians(theta[k]))
    T = np.array([
        [c, s, 0, 0],
        [-s, c, 0, 0],
        [0, 0, c, s],
        [0, 0, -s, c]
    ])
    k1 = E * A / L
    k_global.append(k1 * np.linalg.inv(T) @ K_unit @ T)

# Assemble global stiffness matrix
NDoF = 2 * nodes.shape[0]
K_global = np.zeros((NDoF, NDoF))
K_element = []

for m in range(n):
    N1 = elems[m, 0]
    N2 = elems[m, 1]
    i1, i2 = int(2*N1 - 2), int(2*N1 - 1)
    i3, i4 = int(2*N2 - 2), int(2*N2 - 1)
    ii = [i1, i2, i3, i4]

    A = np.zeros((NDoF, NDoF))
    for k in range(4):
        for l in range(4):
            A[ii[k], ii[l]] = k_global[m][k, l]

    K_global += A
    K_element.append(A)

# Calculate displacements
K_red = K_global.copy()
for k in range(NDoF):
    for l in range(NDoF):
        if rests[k] == 1 or rests[l] == 1:
            K_red[k, l] = 1.0 if k == l else 0.0

u = np.linalg.inv(K_red) @ F

# Calculate reaction forces
R = K_global @ u

# Calculate axial forces
AF = np.zeros(n)
for k in range(n):
    F_ele = K_element[k] @ u
    N1 = elems[k, 0]
    i1, i2 = int(2*N1 - 2), int(2*N1 - 1)
    AF[k] = np.dot(F_ele[[i1, i2]], [-np.cos(np.radians(theta[k])), -np.sin(np.radians(theta[k]))])

print(u)
print(R)
print(AF)
