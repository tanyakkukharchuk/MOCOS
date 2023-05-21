import numpy as np
import warnings
from matplotlib import MatplotlibDeprecationWarning
import matplotlib.pyplot as plt
import time

warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)

def fourier_coefficient(x, k):
    N = len(x)
    Ak = np.sum(x * np.cos(np.pi*k*np.arange(N)/N))
    Bk = np.sum(x * np.sin(np.pi*k*np.arange(N)/N))
    Ck = Ak - 1j*Bk
    num_ops = 8*N +2 # кількість операцій
    num_ops2 = 2*N
    return Ck, num_ops, num_ops2

def discrete_fourier_transform(x):
    N = len(x)
    C = np.zeros(N, dtype=np.complex128)
    mult = 0
    sum = 0
    for k in range(N):
        C[k], num_ops, num_ops2 = fourier_coefficient(x, k)
        mult +=num_ops
        sum += num_ops2
    return mult, sum ,C

# генеруємо масив випадкових даних
x = np.random.rand(200)

# замір часу на початку
start_time = time.time()

# обчислюємо ДПФ
mult, sum, C = discrete_fourier_transform(x)

# обчислення спектру амплітуд
amplitude_spectrum = abs(C)

# обчислення спектру фаз
phase_spectrum = np.angle(C)

# побудова графіку спектру амплітуд
plt.figure(figsize=(8, 6))
plt.stem(amplitude_spectrum, use_line_collection=True)
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.title('Amplitude Spectrum')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.show()

# побудова графіку спектру фаз
plt.figure(figsize=(8, 6))
plt.stem(phase_spectrum, use_line_collection=True)
plt.xlabel('Frequency')
plt.ylabel('Phase')
plt.title('Phase Spectrum')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.show()

# вивід коефіцієнтів Фур'є
for k in range(len(C)):
    print(f"C[{k}] = {C[k]}")

# вивід часу виконання
end_time = time.time()
print(f"Кількість операцій(+): {sum}")
print(f"Кількість операцій(*): {mult}")
print(f"Час обчислення: {end_time - start_time:.5f}")