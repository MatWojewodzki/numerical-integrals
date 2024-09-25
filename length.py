import numpy as np

x_values = np.linspace(-2, 4, 1000)


def f(x: float) -> float:
    return x ** 3 - 3 * x ** 2 + 2 * x - 1


vfunc: callable = np.vectorize(f)

y_values = vfunc(x_values)


def calc_segment_length(prev_x: int, prev_y: int, new_x: int, new_y: int) -> float:
    return np.sqrt((new_x - prev_x) ** 2 + (new_y - prev_y) ** 2)


total_length: float = 0.
for i in range(1, len(x_values)):
    total_length += calc_segment_length(x_values[i - 1], y_values[i - 1], x_values[i], y_values[i])

print(f'Total length: {total_length:.3f}')
