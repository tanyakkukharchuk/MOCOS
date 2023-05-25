import math
import random
import matplotlib.pyplot as plt
from matplotlib import MatplotlibDeprecationWarning
import warnings

warnings.filterwarnings("ignore", category=MatplotlibDeprecationWarning)

def generate_sequence(N, A, n, phi):
    sequence = []
    x_values = []
    interval = 2 * math.pi / N
    x = 0
    for i in range(N):
        deviation = random.uniform(-0.05 * A, 0.05 * A)  # Випадкове відхилення
        y = A * math.sin(n * x + phi) + deviation
        sequence.append(y)
        x_values.append(x)
        x += interval
    return sequence, x_values


def arithmetic_mean(sequence):
    return sum(sequence) / len(sequence)


def harmonic_mean(sequence):
    return len(sequence) / sum(1 / x for x in sequence)


def geometric_mean(sequence):
    non_zero_sequence = [x for x in sequence if x != 0]
    if len(non_zero_sequence) == 0:
        return 0
    return math.prod(non_zero_sequence) ** (1 / len(non_zero_sequence))


def plot_sequence(x_values, *sequences, labels=None):
    for sequence in sequences:
        plt.plot(x_values, sequence, linewidth=0.8)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Sequence Plot')
    if labels is not None:
        plt.legend(labels)
    plt.show()


def exact_value(A, n, x, phi):
    return A * math.sin(n * x + phi)


def compare_values(approximate, exact):
    absolute_error = abs(approximate - exact)
    relative_error = absolute_error / abs(exact) * 100
    return absolute_error, relative_error


# Задані параметри
n = 14
N = n * 100
A = 1
phi = math.pi / 4

# Генерація послідовності
sequence, x_values = generate_sequence(N, A, n, phi)

# Обчислення середніх значень
arithmetic_mean_value = arithmetic_mean(sequence)
harmonic_mean_value = harmonic_mean(sequence)
geometric_mean_value = geometric_mean(sequence)

# Виведення результатів
print("Arithmetic Mean:", arithmetic_mean_value)
print("Harmonic Mean:", harmonic_mean_value)
print("Geometric Mean:", geometric_mean_value)

# Графік послідовності та функції
plot_sequence(x_values, sequence, [arithmetic_mean_value] * len(x_values),
              [harmonic_mean_value] * len(x_values), [geometric_mean_value] * len(x_values),
              labels=["Sequence", "Arithmetic Mean", "Harmonic Mean", "Geometric Mean"])

# Порівняння значень
exact = exact_value(A, n, x_values[0], phi)
approximate = arithmetic_mean_value  # Обрати одне зі значень для порівняння
abs_error, rel_error = compare_values(approximate, exact)
print("Absolute Error:", abs_error)
print("Relative Error:", rel_error)
