import numpy as np
import matplotlib.pyplot as plt
from sympy import Piecewise, symbols, integrate, lambdify

# Define symbolic variable and piecewise function
x = symbols('x')
# piecewise_function = Piecewise(
#     (-2, (1 < x) & (x <= 2)),
#     (1, (2 < x) & (x <= 4)),
#     (1, (6 < x) & (x <= 10)),
#     (-2, (10 < x) & (x <= 12)),
#     (0, True)  # Default case
# )

# piecewise_function = Piecewise(
#     (1, (1 < x) & (x <= 3)),
#     (-1, (5 < x) & (x <= 7)),
#     (2, (9 < x) & (x <= 10)),
#     (-1, (10 < x) & (x <= 12)),
#     (0, True)  # Default case
# )

# piecewise_function = Piecewise(
#     (2, (1 < x) & (x <= 2)),
#     (-1, (4 < x) & (x <= 8)),
#     (2, (10 < x) & (x <= 11)),
#     (0, True)  # Default case
# )

piecewise_function = Piecewise(
    (3*x-3, (1 < x) & (x <= 2)),
    (3, (2 < x) & (x <= 8)),
    (-6, (8 < x) & (x <= 10)),
    (3*x-36, (10 < x) & (x <= 12)),
    (0, True)  # Default case
)

# piecewise_function = Piecewise(
#     (4, (1 < x) & (x <= 3)),
#     (-1, (4 < x) & (x <= 8)),
#     (-1, (9 < x) & (x <= 13)),
#     (0, True)  # Default case
# )

# Default case used in lecture.
# piecewise_function = Piecewise(
#     (-2, (2 < x) & (x <= 3)),
#     (1, (3 < x) & (x <= 5)),
#     (0, True)  # Default case
# )

# piecewise_function = Piecewise(
#     (-x+2.5, (1 < x) & (x <= 4)),
#     (0, True)  # Default case
# )

# Compute the first integral
first_integral = integrate(piecewise_function, x)

# Compute the second integral
second_integral = integrate(first_integral, x)

# Compute the second integral
third_integral = integrate(second_integral, x)

# Convert symbolic functions to numerical functions
piecewise_lambdified = lambdify(x, piecewise_function, 'numpy')
first_integral_lambdified = lambdify(x, first_integral, 'numpy')
second_integral_lambdified = lambdify(x, second_integral, 'numpy')
third_integral_lambdified = lambdify(x, third_integral, 'numpy')

# Generate x values
x_values = np.linspace(0, 14, 1200)

# Compute y_values, first_integral_values, and second_integral_values
y_values = piecewise_lambdified(x_values)
first_integral_values = first_integral_lambdified(x_values)
second_integral_values = second_integral_lambdified(x_values)
third_integral_values = third_integral_lambdified(x_values)

# Plot the original piecewise function, its first integral, and its second integral
plt.figure(figsize=(12, 9))

# Plot the piecewise function
plt.subplot(3, 1, 1)
plt.plot(x_values, y_values, label='Piecewise Function', color='blue')
plt.title('Piecewise Function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Plot the first integral
plt.subplot(3, 1, 2)
plt.plot(x_values, first_integral_values, label='First Integral', color='green')
plt.title('First Integral of Piecewise Function')
plt.xlabel('x')
plt.ylabel('Integral of f(x)')
plt.legend()
plt.grid(True)

# Plot the second integral
plt.subplot(3, 1, 3)
plt.plot(x_values, -second_integral_values, label='Second Integral', color='red')
plt.title('Second Integral of Piecewise Function')
plt.xlabel('x')
plt.ylabel('Integral of Integral of f(x)')
plt.legend()
plt.grid(True)

# Plot the second integral
# plt.subplot(4, 1, 4)
# plt.plot(x_values, (second_integral_values * 0.5)-1, label='Third Integral', color='magenta')
# plt.plot(x_values, (second_integral_values * 0.5)+1, label='Third Integral', color='magenta')
# plt.plot(x_values, (second_integral_values * 0.5)+1, label='Third Integral', color='magenta')
# plt.title('Second Integral of Piecewise Function')
# plt.xlabel('x')
# plt.ylabel('Integral of Integral of f(x)')
# plt.legend()
# plt.grid(True)

plt.tight_layout()
plt.show()
