import matplotlib.pyplot as plt
import numpy as np

# Ranglar ro'yxati
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#A633FF']

# Ranglar sxemasini chizish
n = len(colors)
angle = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
angle += angle[:1]
colors += colors[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angle, [1] * (n + 1), color=colors[0], alpha=0.25)
ax.plot(angle, [1] * (n + 1), color=colors[0], linewidth=2)

for i in range(1, n):
    ax.fill(angle, [i/n] * (n + 1), color=colors[i], alpha=0.25)
    ax.plot(angle, [i/n] * (n + 1), color=colors[i], linewidth=2)

ax.set_yticklabels([])
ax.set_xticks(angle[:-1])
ax.set_xticklabels([f'Color {i+1}' for i in range(n)])
ax.set_title('Color Harmony Representation', size=20, color='black', va='bottom')
plt.show()
