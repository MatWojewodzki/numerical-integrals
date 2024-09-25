import numpy as np

start = 0
stop = 0.877
steps_count = 1000

dx = (stop - start) / steps_count

steps = np.linspace(start, stop, steps_count)
sinus_values = np.sin(steps)
sin_area = sinus_values.sum() * dx

square_values = np.square(steps)
square_area = square_values.sum() * dx

area_diff = abs(square_area - sin_area)

print(f'Area: {area_diff:.2f}')
