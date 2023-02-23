# f(x) = -12x**4*sin(cos(x)) - 18x**3 + 5x**2 + 10x - 30

# 4.Построить график
# 1.Определить корни
# 5.Вычислить вершину
# 2.Найти интервалы, на которых функция возрастает
# 3.Найти интервалы, на которых функция убывает
# 6.Определить промежутки, на котором f > 0
# 7.Определить промежутки, на котором f < 0

import numpy as np
import matplotlib.pyplot as plt

limit = 10
step = 0.001
color = 'b'
lines = '-'
direct_up = True

a, b, c, d, e = -12, -18, 5, 10, -30
x = np.arange(-limit, limit, step)

def switch_color():
    global color
    if color == 'b':
        color = 'r'
    else:
        color = 'b'
    return color

def switch_line():
    global lines
    if lines == '-':
        lines = '--'
    else:
        lines = '-'
    return lines

def func(x): 
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e
  
def take_roots(a, b, c, d, e):
    roots = []
    for i in range(len(x) -1):
        if (func(x[i])>0 and func(x[i+1])<0) or (func(x[i])<0 and func(x[i+1])>0):
            roots.append(round(x[i], 2))
    return roots
            
roots = take_roots(a, b, c, d, e)
   
x_change = [(-limit, 'limit')]
for i in range(len(x) -1):
        if (func(x[i])>0 and func(x[i+1])<0) or (func(x[i])<0 and func(x[i+1])>0):
            x_change.append((round(x[i], 2), 'zero'))
        if direct_up:
            if func(x[i]) > func(x[i+1]):
                x_change.append((round(x[i], 2), 'direct'))
                direct_up = False
        else:
            if func(x[i]) < func(x[i+1]):
                x_change.append((round(x[i], 2), 'direct'))
                direct_up = True
x_change.append((limit, 'limit'))
                
min_y = min(func(x))
min_x = -limit
for x in x_change:
    if x[1] in ['direct','limit']:
        if abs(func(x[0]) - min_y) < abs(min_x - min_y):
            min_x = x[0]

for i in range(len(x_change)-1):
    cur_x = np.arange(x_change[i][0], x_change[i+1][0] + step, step)
    if x_change[i][1] == 'zero':
        plt.rcParams['lines.linestyle'] = switch_line()
        plt.plot(cur_x, func(cur_x), color)
    else:
        plt.plot(cur_x, func(cur_x), switch_color())

for item in roots:
    plt.plot(item, func(item), 'gx')

plt.plot(min_x, min_y, 'co', label=f'Экстремум функции: ({round(min_x, 2)}, {round(min_y, 2)})')
plt.rcParams['lines.linestyle'] = '-'
plt.plot(0, 0, 'b', label='Убывание > 0')
plt.plot(0, 0, 'r', label='Возрастание > 0')
plt.rcParams['lines.linestyle'] = '--'
plt.plot(0, 0, 'b', label='Убывание < 0')
plt.plot(0, 0, 'r', label='Возрастание < 0')
plt.title(f'Корни на промежутке [{-limit};{limit}]: {roots}')
plt.legend()
plt.grid()
plt.show()    
