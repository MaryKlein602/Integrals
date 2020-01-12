from tabulate import tabulate

f = open('Integral(Euler).txt', 'w')
f.write('Solution for differential equation with Euler method\n\n')
f.write('The equation is: y + 3y / x = 4x\n')
f.write('The steps are: h = 0,1, h = 0,2\n')
f.write('The points are: y(1) = 3, so x = 1\n\n')
f.write('So the x belongs to [1, 1,4]\n')
f.write('The solution is: y(0) = ( x**5 + 2) / x**3\n\n')


h1 = 0.1
h2 = 0.2
x0 = [1, 1.1, 1.2, 1.3, 1.4]
y0 = [(i**5 + 2) / i**3 for i in x0]

f.write('So the values are: x = {0}\n {1} y = {2}\n\n'.format(x0, ' '*17, y0))
f.write('By Eulers formula y1 = y0 + h * f(x0, y0)\n')
f.write("y' = 4x - 3y/x")


def euler_solution(x, y, h):
    y1 = []

    for i in range(len(x)):

        y1_i = y[i] + h * (4 * x[i] - (3 * y[i] / x[i]))
        f.write('y1 = {0} + {1} * (4 * {2} - (3 * {0} / {2}))\n'.format(y[i], h, x[i]))
        f.write('{0} + {1} * (4 * {2} - (3 * {0} / {2})) = {3}\n\n'.format(y[i], h, x[i], y1_i))

        y1.append(y1_i)
    return y1

f.write('For step: h = 0,1\n')
y1_1 = euler_solution(x0, y0, h1)
f.write('\n For step: h = 0,2\n')
y1_2 = euler_solution(x0, y0, h2)



f.write('The result:\n')

results = [(x0[i], y0[i], y1_1[i], y1_2[i]) for i in range(len(x0))]
f.write(tabulate(results, headers=["x0", "y0", "y' h=0,1", "y' h=0,2"]))
f.close()
