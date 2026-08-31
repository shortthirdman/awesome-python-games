import plotext as plt
import random
import time

def next_value(previous, volatility=3, floor=0, ceiling=100):
    change = random.uniform(-volatility, volatility)
    return min(ceiling, max(floor, previous + change))

cpu_history = [40]
memory_history = [55]
alert_ticks = []

for tick in range(50):
    cpu_history.append(next_value(cpu_history[-1], volatility=6))
    memory_history.append(next_value(memory_history[-1], volatility=3))
    if len(cpu_history) > 35:
        cpu_history = cpu_history[-35:]
        memory_history = memory_history[-35:]
    if cpu_history[-1] > 85:
        alert_ticks.append(tick)
    plt.clf()
    plt.theme("dark")
    plt.title("Live Server Metrics Simulation")
    plt.xlabel("Time (ticks)")
    plt.ylabel("Usage %")
    plt.plot(cpu_history, label="CPU", color="cyan", marker="dot")
    plt.plot(memory_history, label="Memory", color="magenta", marker="dot")
    plt.hline(85, color="red")
    plt.ylim(0, 100)
    plt.show()
    time.sleep(0.1)

print(f"\nSimulation finished. CPU crossed the danger threshold {len(alert_ticks)} times.")

plt.clf()
plt.theme("dark")
plt.title("Final Simulation Summary")
plt.bar(
    ["Peak CPU", "Peak Memory", "Alerts Triggered"],
    [max(cpu_history), max(memory_history), len(alert_ticks)],
    color=["cyan", "magenta", "red"],
)
plt.show()