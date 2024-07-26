import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Grafik penceresini oluşturma
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', animated=True)

# Eksen sınırlarını ayarlama
def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

# Güncelleme fonksiyonu
def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

# Animasyonu başlatma
ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                              init_func=init, blit=True)

plt.show()
