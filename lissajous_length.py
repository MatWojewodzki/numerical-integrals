import numpy as np

segments: int = 1000

alpha: np.ndarray = np.linspace(0, 2 * np.pi, segments)
x: np.ndarray = np.cos(3 * alpha)
y: np.ndarray = np.sin(2 * alpha)


def calc_segment_length(prev_x: int, prev_y: int, new_x: int, new_y: int) -> float:
    return np.sqrt((new_x - prev_x) ** 2 + (new_y - prev_y) ** 2)


total_length: float = 0.

for i in range(1, len(alpha)):
    total_length += calc_segment_length(x[i - 1], y[i - 1], x[i], y[i])

print(f'Total curve length: {total_length:.3f}')
