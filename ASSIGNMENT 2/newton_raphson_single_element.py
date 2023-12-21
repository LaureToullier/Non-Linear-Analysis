import numpy as np
import matplotlib.pyplot as plt

# Constitutive relationship
eps_0 = 0.003
sigma_0 = 500

eps_vec = np.linspace(0, eps_0 * 1.1, 101)
sigma = sigma_0 / 2 * (3 * eps_vec / eps_0 - (eps_vec / eps_0) ** 3)

# Member properties
Length = 2
Area = 0.01

# Load vector
N_load_steps = 2
Pmax = Area * sigma_0 * 0.95
P = np.linspace(Pmax / N_load_steps, Pmax, N_load_steps)

# Maximum number of iterations per load step & tolerance
N_iter_max = 20
tol = sigma_0 * Area / 1e5

plt.figure()
U = [0]
tot_iter = 0
U_vec = []
Pr_vec = []

for n in range(N_load_steps):
    print(f"Loadstep {n+1} (U [mm], Pr [MN], R [MN]):")
    U_iter = [U[-1]]

    for j in range(N_iter_max):
        u = U_iter[j]
        p = Area * sigma_0 / 2 * (3 * u / (eps_0 * Length) - (u / (eps_0 * Length)) ** 3)
        Pr = p
        R = P[n] - Pr

        print(f"{U_iter[j]*1000:.3f} {Pr:.3f} {R:.3f}")

        if j > 0:
            plt.plot([U_iter[j], U_iter[j]], [P[n], Pr], 'r.-', label='Iterations')

        if abs(R) < tol:
            break

        Kt = 3 / 2 * Area * sigma_0 / (eps_0 * Length) * (1 - (u / (Length * eps_0)) ** 2)
        U_iter.append(U_iter[j] + R / Kt)

        plt.plot([U_iter[j], U_iter[-1]], [Pr, P[n]], 'r.-')

    U.append(U_iter[-1])
    U_vec.append(U_iter[-1])
    Pr_vec.append(Pr)

    if abs(R) > tol and j == N_iter_max - 1:
        print("Number of maximum iterations reached but no convergence")

    tot_iter += j + 1

plt.xlim([0, max(U_vec) * 1.1])
plt.xlabel('Basic displ. [mm]')
plt.ylabel('Basic force [kN]')
final_line, = plt.plot([0] + U_vec, [0] + list(P), 'bx-', label='Final solution')
exact_line, = plt.plot(eps_vec * Length, sigma * Area, 'k-', label='Exact solution')

for p in P:
    plt.plot([0, U_vec[-1]], [p, p], 'k--')

handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.savefig('Single_element.png')
plt.show()

