import numpy as math
from scipy import integrate
import matplotlib.pyplot as plot
from prettytable import PrettyTable


def function(x):
    return x ** 14 * math.exp(-x ** 2 / 14)


def a_kIntegral(x, k):
    return (2 / intervalLength) * function(x) * math.cos(k * x)


def a_kCoefficient(k):
    a_k = integrate.quad(a_kIntegral, interval[0], interval[1], args=k)
    return a_k[0]


def calculatingHarmonic(x, k):
    return a_kCoefficient(k) * math.cos(k * x) + b_k


def calculatingApproximation(x, number):
    return a_kCoefficient(0) / 2 + sum(calculatingHarmonic(x, k) for k in range(1, number + 1))


def calculatingMistake(x):
    try:
        return (calculatingApproximation(x, N) - function(x)) / function(x)
    except RuntimeWarning:
        return 0


def messages(text, file):
    print(text)
    file.write(text + "\n")


def showCoefficients(file):
    th, td = ['№', 'a_k', 'b_k'], []
    messages("\nКоефіцієнти ряду Фур'є", file)
    for i in range(0, N + 1):
        td.append(i)
        td.append((str(round(a_kCoefficient(i), 4))))
        if i == 0:
            td.append("Не існує")
        else:
            td.append(str(b_k))
    columns = len(th)
    table = PrettyTable(th)
    file.write('  №        a_k         b_k'.format(*td[:columns]) + "\n")
    while td:
        table.add_row(td[:columns])
        file.write('  {0:<3}   {1:<12} {2:<12}'.format(*td[:columns]) + "\n")
        td = td[columns:]
    print(table)


def showGraphs(start, end):
    graph1, ax1 = plot.subplots(1, 1, figsize=(10, 10))
    ax1.set_title("Графік функції f та наближення функції рядом Фур'є", fontsize=16)
    plot.grid(True)
    x_1 = math.linspace(start, end, num=1000)
    plot.plot(x_1, function(x_1), label="f", linewidth=3)
    plot.plot(x_1, calculatingApproximation(x_1, N), label="N = " + str(10), color="green")
    plot.xlim([start, end])
    plot.legend(borderaxespad=0.2, loc="best")
    plot.show()

    graph2, ax2 = plot.subplots(figsize=(10, 10))
    ax2.set_title('Функція a(k) в частотній області', fontsize=16)
    plot.grid(True)
    for i in range(0, N + 1):
        plot.plot([i, i], [0, a_kCoefficient(i)], 'bo-')
    plot.show()

    graph3, ax3 = plot.subplots(figsize=(10, 10))
    ax3.set_title('Функція b(k) в частотній області', fontsize=16)
    plot.grid(True)
    for i in range(1, N + 1):
        plot.plot(i, b_k, 'bo-')
    plot.show()

    graph4, ax4 = plot.subplots(1, 1, figsize=(10, 10))
    ax4.set_title("Графік функції f та поступове наближення функції рядом Фур'є", fontsize=16)
    plot.grid(True)
    x_2 = math.linspace(start, end, num=1000)
    plot.xlim([start, end])
    plot.plot(x_2, function(x_2), label="Функція f")
    for i in range(1, N + 1):
        plot.plot(x_2, calculatingApproximation(x_2, i), label="Наближення N = " + str(i))
    plot.legend(borderaxespad=0.2, loc="best")
    plot.show()

    graph5, ax5 = plot.subplots(1, 1, figsize=(10, 10))
    ax5.set_title("Графік відносної похибки апроксимації", fontsize=16)
    plot.grid(True)
    x_3 = math.linspace(start + 0.01, end - 0.01, num=2500)
    plot.xlim([start, end])
    plot.plot(x_3, (calculatingApproximation(x_3, N) - function(x_3)) / function(x_3), label="Значення відносної похибки")
    plot.legend(borderaxespad=0.2, loc="best")
    plot.show()


interval = [-3*math.pi, 3*math.pi]
intervalLength, N, b_k = interval[1] - interval[0], 10, 0
file = open("result.txt", "w", encoding="utf-8")

messages("Обчислення наближеня за допомогою ряду Фур'є значення функції x^10 * e^(-x^2 / 10), на проміжку х є [{}; {}]".format(interval[0], interval[1]), file)
messages("\nПорядок N = {}".format(str(N)), file)
showGraphs(interval[0], interval[1])
showCoefficients(file)
file.close()