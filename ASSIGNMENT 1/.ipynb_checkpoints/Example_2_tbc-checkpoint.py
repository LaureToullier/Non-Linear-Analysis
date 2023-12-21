# This file is part of the Nonlinear analysis of structures (CIVIL-449) course at EPFL taught by the EESD and RESLAB. % Disclaimer: This file does represent best practice in coding. In fact, it has been coded in a bad way (hard-coded) and the assignment 1 is to generalise this code so that it works for any 2D truss geometry. % The author of this file: Hnat Lesiv (hnat.lesiv@epfl.ch)

import numpy as np

# Element connectivity 
connectivity = np.array([[1, 4], [2, 4], [3, 4]])

# Unit stiffness matrix of bar in local coordinate system
K_unit = np.array([[1, 0, -1, 0], 
                   [0, 0,  0, 0], 
                   [-1, 0, 1, 0], 
                   [0, 0, 0, 0]])

# Input data and element stiffness matrices
E = 200e3  # N/mm^2

# Bar 1
theta1 = -45
c = np.cos(np.radians(theta1))
s = np.sin(np.radians(theta1))
T = np.array([[c, s, 0, 0], 
              [-s, c, 0, 0], 
              [0, 0, c, s], 
              [0, 0, -s, c]])
A = 10e3  # mm^2
L = np.sqrt(2)*2000  # mm
k1 = E * A / L
k1_global = k1 * T.T @ K_unit @ T

# Fill in the information for Bar 2
"""

"""

# And the same for Bar 3
"""

"""


# Assemble global stiffness matrix
NDoF = 8
K_global = np.zeros((NDoF, NDoF))
K_element_8DOF = []

# Assemble 1st element
K1_global = np.zeros((NDoF, NDoF))
K1_global[0:2, 0:2] = k1_global[0:2, 0:2]
"""

"""

# Assemble 2nd element
"""

"""

# Assemble 3rd element
"""

"""

# Calculate displacements at Node 4
F_red = np.array([-3000, -18000]) * 1000  # N
K_red = K_global[6:8, 6:8]
u_red = np.linalg.inv(K_red) @ F_red

# Calculate reaction forces at Nodes 1, 2, 3
u_vec = np.array([0, 0, 0, 0, 0, 0, u_red[0], u_red[1]])
F = K_global @ u_vec

# Calculate axial forces
F_ele = K_element_8DOF[0] @ u_vec
"""

"""

# Calculate axial forces for 2nd element

# Calculate axial forces for 3rd element
