from noise.PerlinNoise import PerlinNoise
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import logging


def plot_perlin_noise(perlin_noise, size=50, scale=0.1, octaves=3, persistence=0.5, x_offset=0.0, y_offset=0.0, z_offset=0.0):
    x = np.linspace(0, scale, size)
    y = np.linspace(0, scale, size)
    z = np.linspace(0, scale, size)

    data = np.zeros((size, size, size))

    for i in range(size):
        for j in range(size):
            for k in range(size):
                data[i, j, k] = perlin_noise.octave_perlin(x[i] + x_offset, y[j] + y_offset, z[k] + z_offset, octaves, persistence)

    # Create a subplot with 3D surface plot
    fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])

    # Add 3D surface plot
    fig.add_trace(go.Surface(z=data[:, :, 0]), row=1, col=1)

    # Show the plot
    fig.show()


def main():
    perlin_noise = PerlinNoise()
    plot_perlin_noise(perlin_noise, x_offset=0.5)


if __name__ == '__main__':
    main()
