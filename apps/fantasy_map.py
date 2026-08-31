import random
from perlin_noise import PerlinNoise
from colorama import init, Fore, Style

init(autoreset=True)
WIDTH, HEIGHT = 80, 30

noise = PerlinNoise(octaves=4, seed=random.randint(1, 9999))
elevation_map = []
for y in range(HEIGHT):
    row = []
    for x in range(WIDTH):
        value = noise([x / WIDTH, y / HEIGHT])
        row.append(value)
    elevation_map.append(row)

def render_tile(value):
    if value < -0.15:
        return Fore.BLUE + "~"
    elif value < -0.02:
        return Fore.CYAN + "="
    elif value < 0.05:
        return Fore.GREEN + "."
    elif value < 0.12:
        return Fore.GREEN + Style.BRIGHT + "^"
    elif value < 0.2:
        return Fore.YELLOW + "n"
    else:
        return Fore.WHITE + Style.BRIGHT + "#"

print(Style.BRIGHT + "A Procedurally Generated Fantasy Map\n")
for row in elevation_map:
    line = "".join(render_tile(value) for value in row)
    print(line)

print(Style.RESET_ALL)
print("\nLegend: ~ water   = shallows   . plains   ^ hills   n forest   # mountains")

lowest = min(min(row) for row in elevation_map)
highest = max(max(row) for row in elevation_map)
print(f"Elevation range this run: {lowest:.3f} to {highest:.3f}")

water_tiles = sum(1 for row in elevation_map for v in row if v < -0.15)
total_tiles = WIDTH * HEIGHT
print(f"Water coverage: {water_tiles / total_tiles * 100:.1f}% of this map")