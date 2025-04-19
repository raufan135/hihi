import matplotlib.pyplot as plt
import numpy as np

# Define scale: 1 unit = 10 N
# Compute vectors in plot units
F = np.array([20, 0]) / 10
P = np.array([10 * np.cos(np.deg2rad(30)), 10 * np.sin(np.deg2rad(30))]) / 10
R = np.array([50 * np.cos(np.deg2rad(-60)), 50 * np.sin(np.deg2rad(-60))]) / 10
sum_FP = F + P

plt.figure()
# Plot vectors
plt.arrow(0, 0, F[0], F[1], head_width=0.1, length_includes_head=True)
plt.text(F[0], F[1], 'F (20 N)', fontsize=12)

plt.arrow(0, 0, P[0], P[1], head_width=0.1, length_includes_head=True)
plt.text(P[0], P[1], 'P (10 N, 30°)', fontsize=12)

plt.arrow(0, 0, R[0], R[1], head_width=0.1, length_includes_head=True)
plt.text(R[0], R[1], 'R (50 N, -60°)', fontsize=12)

plt.arrow(0, 0, sum_FP[0], sum_FP[1], head_width=0.1, length_includes_head=True)
plt.text(sum_FP[0], sum_FP[1], 'F + P', fontsize=12)

# Axes and grid
plt.axhline(0, linewidth=0.5)
plt.axvline(0, linewidth=0.5)
plt.gca().set_aspect('equal', 'box')
plt.grid(True)

# Labels
plt.title('Vektor F, P, R, dan F+P (Skala: 1 unit = 10 N)')
plt.xlabel('Sumbu x (unit)')
plt.ylabel('Sumbu y (unit)')

plt.show()
