import numpy as np

class ParticleclassR1:
    def __init__(self, m,v,r):
        self.m = m
        self.v = np.array(v)
        self.r = np.array(r)
    def update_positionR1(self, dt):
        self.r += self.v*dt

n_deeltjes = 10
dt = 0.25
particle_arrayR1=[]
x_startR1 = []
y_startR1 = []
for i in range(n_deeltjes):
    start_x = float(i)
    randomvx = np.random.uniform(-5,5)
    particle_arrayR1.append(ParticleclassR1(m=1,v=[randomvx, 0.0], r=[start_x, 0.0]))
x_eind = [p.r[0] for p in particle_array]
y_eind = [p.r[1] for p in particle_array]


plt.figure(figsize=(10, 4))
plt.scatter(
    x_start, y_start, color="blue", s=80, label="Startpositie", zorder=3
)
plt.scatter(
    x_eind, y_eind, color="red", s=80, label="Eindpositie (na update)", zorder=3
)


for i in range(n_deeltjes):
  plt.plot(
      [x_start[i], x_eind[i]],
      [y_start[i], y_eind[i]],
      color="gray",
      linestyle="--",
      alpha=0.6,
  )


plt.axhline(0, color="black", linewidth=1, linestyle="-")
plt.xlabel("X-positie")
plt.ylabel("Y-positie")
plt.title("Beweging van 10 deeltjes met behulp van ParticleClass (Oefening intro-ex-2)")
plt.legend(loc="upper right")
plt.grid(True, alpha=0.3)
plt.show()

