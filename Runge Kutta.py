from tabulate import tabulate

f = open('Integral(Runge Kutta).txt', 'w')
f.write('Solution for differential equation with Euler method\n\n')
f.write('The equation is: y + 3y / x = 4x\n')
f.write('The steps are: h = 0,1, h = 0,2\n')
f.write('The points are: y(1) = 3, so x = 1\n\n')
f.write('So the x belongs to [1, 1,4]\n')
f.write('The solution is: y(0) = ( x**5 + 2) / x**3\n\n')
f.write("y' = 4x - 3y/x\n\n")

h1 = 0.1
h2 = 0.2
x0 = [1, 1.1, 1.2, 1.3, 1.4]
y0 = [(i**5 + 2) / i**3 for i in x0]

f.write('So the values are: x = {0}\n {1} y = {2}\n\n'.format(x0, ' '*17, y0))
f.write('By Runge-Kutta formula y1 = y0 + h * delta_y\n')
f.write("delta_y = 1/6 * (k1 + 2k2 + 2k3 + k4)\n\n")
f.write('Where: k1 = h * f(x; y) \n{0} k2 = h * f(x + h/2; y + k1/2) \n{0} '
        'k3 = h * f(x + h/2; y + k2/2) \n{0} k4 = h * f(x + h; y + k3)'.format(' '*6))


def count_k1(x, y, h):

    k1 = []
    f.write('\nWe found all k1 coeficients:\n')
    for i in range(len(x)):

        k1_coef = h * (4 * x[i] - 3 * y[i] / x[i])
        f.write('{0} k1({1}) = {2} * (4 * {3} - 3 * {4} / {3})\n'.format(' '*18, i, h, x[i], y[i]))
        f.write('{0} {2} * (4 * {3} - 3 * {4} / {3}) = {1}\n\n'.format(' '*18,k1_coef, h, x[i], y[i]))

        k1.append(k1_coef)

    return k1


def count_k2(x, y, h, k1):

    k2 = []
    f.write('We found all k2 coeficients:\n')
    for i in range(len(x)):

        k2_coef = h * (4 * (x[i] + h/2) - 3 * (y[i] + (k1[i] / 2)) / (x[i] + h/2))
        f.write('{0} k2({1}) = {2} * (4 * ({3} + {2}/2) - 3 * ({4} + ({5} / 2)) / '
                '({3} + {2}/2))\n'.format(' '*18, i, h, x[i], y[i], k1[i]))
        f.write('{0} {2} * (4 * ({3} + {2}/2) - 3 * ({4} + ({5} / 2)) / '
                '({3} + {2}/2)) = {1}\n\n'.format(' '*18, k2_coef, h, x[i], y[i], k1[i]))
        k2.append(k2_coef)
    return(k2)


def count_k3(x, y, h, k2):
    k3 = []
    f.write('We found all k3 coeficients:\n')

    for i in range(len(x)):

        k3_coef = h * (4 * (x[i] + (h / 2)) - 3 * (y[i] + (k2[i] / 2)) / (x[i] + (h / 2)))
        f.write('{0} k2({1}) = {2} * (4 * ({3} + {2}/2) - 3 * ({4} + ({5} / 2)) / '
                '({3} + {2}/2))\n'.format(' ' * 18, i, h, x[i], y[i], k2[i]))
        f.write('{0} {2} * (4 * ({3} + {2}/2) - 3 * ({4} + ({5} / 2)) / '
                '({3} + {2}/2)) = {1}\n\n'.format(' ' * 18, k3_coef, h, x[i], y[i], k2[i]))
        k3.append(k3_coef)

    return (k3)


def count_k4(x, y, h, k3):

    k4 = []
    f.write('We found all k4 coeficients:\n')

    for i in range(len(x)):

        k4_coef = h * (4 * (x[i] + h) - 3 * (y[i] + k3[i]) / (x[i] + h))
        f.write('{0} k2({1}) = {2} * (4 * ({3} + {2}) - 3 * ({4} + {5}) / '
                '({3} + {2}))\n'.format(' ' * 18, i, h, x[i], y[i], k3[i]))
        f.write('{0} {2} * (4 * ({3} + {2}) - 3 * ({4} + {5}) / '
                '({3} + {2})) = {1}\n\n'.format(' ' * 18, k4_coef, h, x[i], y[i], k3[i]))
        k4.append(k4_coef)

    return (k4)


def find_delta(x, y, h):

    k1 = count_k1(x, y, h)
    # print(k1)
    k2 = count_k2(x, y, h, k1)
    # print(k2)
    k3 = count_k3(x, y, h, k2)
    # print(k3)
    k4 = count_k4(x, y, h, k3)
    # print(k4)

    '''delta_y = 1/6 * (k1 + 2k2 + 2k3 + k4'''

    delta_y = []
    f.write('Lets find all delta_y:\n')

    for i in range(len(x)):

        delta = (1 / 6) * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
        f.write('{0} delta[{1}] = 1/6 * ({2} + 2 * {3} + 2 * {4} + '
                '{5})\n'.format(' ' * 22, i, k1[i], k2[i], k3[i], k4[i]))
        delta_y.append(delta)

    return delta_y, k1, k2, k3, k4

def solving_equation(x, y, h):

    y1 = []
    delta_y, k1, k2, k3, k4 = find_delta(x, y, h)
    f.write('\nSo let`s put values to Runge - Kutta equation:\n\n')

    for i in range(len(y)):

        y1_count = y[i] + (h * delta_y[i])
        f.write('{0} y1({1}) = {2} + ({3} * {4})\n'.format(' '*22, i, y[i], h, delta_y[i]))
        f.write('{0} {2} + ({3} * {4}) = {1}\n\n'.format(' '*22, y1_count, y[i], h, delta_y[i]))
        y1.append(y1_count)

    f.write('The result for step h = {}:\n'.format(h))

    results = [(x0[i], y0[i], k1[i], k2[i], k3[i], k4[i], delta_y[i], y1[i]) for i in range(len(x0))]
    f.write(tabulate(results, headers=["x0", "y0", "k1", "k2","k3", "k4","delta_y", "y'"]))



f.write('For step: h = 0,1\n\n')
solving_equation(x0, y0, h1)
f.write('\n For step: h = 0,2\n\n')
solving_equation(x0, y0, h2)


f.close()