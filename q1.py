
import numpy as np
import matplotlib.pyplot as plt


m = 20.0
k = 20.0
h = 1.0
t = np.arange(0, 16, h)


def rk4(c):
    x = np.zeros(len(t))
    v = np.zeros(len(t))

    x[0] = 1.0
    v[0] = 0.0

    def f1(x, v):
        return v

    def f2(x, v):
        return -(c/m)*v - (k/m)*x

    for i in range(len(t)-1):
        K1x = h*f1(x[i], v[i])
        K1v = h*f2(x[i], v[i])

        K2x = h*f1(x[i]+K1x/2, v[i]+K1v/2)
        K2v = h*f2(x[i]+K1x/2, v[i]+K1v/2)

        K3x = h*f1(x[i]+K2x/2, v[i]+K2v/2)
        K3v = h*f2(x[i]+K2x/2, v[i]+K2v/2)

        K4x = h*f1(x[i]+K3x, v[i]+K3v)
        K4v = h*f2(x[i]+K3x, v[i]+K3v)

        x[i+1] = x[i] + (
            K1x + 2*K2x + 2*K3x + K4x
        )/6

        v[i+1] = v[i] + (
            K1v + 2*K2v + 2*K3v + K4v
        )/6

    return x, v


results = {}

for c in [5, 40, 60]:
    results[c] = rk4(c)

    print("\nDamping coefficient =", c)
    print("Time(s)     Displacement(m)     Velocity(m/s)")

    x, v = results[c]
    for i in range(len(t)):
        print(f"{t[i]:5.1f}       {x[i]: .8f}        {v[i]: .8f}")

for c in [5, 40, 60]:
    plt.plot(t, results[c][0], marker='o',
             markersize=3, label=f'c = {c} Ns/m')

plt.xlabel("Time (s)")
plt.ylabel("Displacement x (m)")
plt.title("Damped Spring-Mass System using RK4")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
