
import numpy as np
import matplotlib.pyplot as plt

h = 0.1
t = np.arange(0, 1.0 + h/2, h)
N = len(t)


y_exp = np.zeros(N)
y_imp = np.zeros(N)

y_exp[0] = 1.0
y_imp[0] = 1.0

for n in range(N-1):
    y_exp[n+1] = y_exp[n] + h*(-10*y_exp[n])


for n in range(N-1):
    y_imp[n+1] = y_imp[n]/(1 + 10*h)

y_exact = np.exp(-10*t)


print("t       Analytical     Explicit       Implicit")
for i in range(N):
    print(f"{t[i]:.1f}    {y_exact[i]:.8f}   "
          f"{y_exp[i]:.8f}   {y_imp[i]:.8f}")


plt.plot(t, y_exact, marker='o', label='Analytical')
plt.plot(t, y_exp, marker='s', label='Explicit Euler')
plt.plot(t, y_imp, marker='^', label='Implicit Euler')

plt.xlabel("Time (s)")
plt.ylabel("y(t)")
plt.title("Comparison of Euler Methods")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

