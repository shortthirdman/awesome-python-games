from PIL import Image
import numpy as np

WIDTH, HEIGHT = 900, 700
MAX_ITER = 200
x_min, x_max = -2.5, 1.0
y_min, y_max = -1.25, 1.25
x = np.linspace(x_min, x_max, WIDTH)
y = np.linspace(y_min, y_max, HEIGHT)
real, imag = np.meshgrid(x, y)
c = real + imag * 1j
z = np.zeros_like(c)
divergence_step = np.zeros(c.shape, dtype=int)

for iteration in range(MAX_ITER):
    mask = np.abs(z) <= 2
    z[mask] = z[mask] ** 2 + c[mask]
    divergence_step[mask & (np.abs(z) > 2)] = iteration

def make_palette():
    palette = []
    for i in range(256):
        t = i / 255
        r = int(9 * (1 - t) * t ** 3 * 255)
        g = int(15 * (1 - t) ** 2 * t ** 2 * 255)
        b = int(8.5 * (1 - t) ** 3 * t * 255)
        palette.append((min(r, 255), min(g, 255), min(b, 255)))
    return palette

palette = make_palette()
max_step = divergence_step.max() if divergence_step.max() > 0 else 1
normalized = (divergence_step / max_step * 255).astype(int)
normalized[divergence_step == 0] = 0
image = Image.new("RGB", (WIDTH, HEIGHT))
pixels = image.load()

for py in range(HEIGHT):
    for px in range(WIDTH):
        color_index = normalized[py, px]
        pixels[px, py] = palette[color_index]

image.save("mandelbrot.png")
print("Saved mandelbrot.png, open it to see the fractal")

preview = image.resize((300, 233))
preview.save("mandelbrot_preview.png")
print("Also saved a smaller preview version for quick sharing")