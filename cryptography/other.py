REAL_PASSWORD = "SuperLongP@ssw0rd2026!WithNumbers&Symbols99"

def check_password(stored, provided):
    if len(stored) != len(provided):
        return False
    for i in range(len(stored)):
        if stored[i] != provided[i]:
            return False
    return True

import time
import statistics

def measure(guess, runs=2000):
    times = []
    for _ in range(runs):
        start = time.perf_counter_ns()
        check_password(REAL_PASSWORD, guess)
        end = time.perf_counter_ns()
        times.append(end - start)
    return statistics.mean(times), statistics.stdev(times)

candidates = [
    "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",          # wrong immediately
    "SuperLongP@ssw0rd00000000000000000000000000",           # correct up to ~
    "SuperLongP@ssw0rd20260000000000000000000000",           # more correct
    "SuperLongP@ssw0rd2026!WithNumbers0000000000",           # even more
    "SuperLongP@ssw0rd2026!WithNumbers&Symbols00",           # almost
    "SuperLongP@ssw0rd2026!WithNumbers&Symbols99",           # correct
]

print("Guess (prefix shown)".ljust(45), "Avg (ns)", "Std dev", "       Diff")
print("-" * 80)

baseline = None
base_value = 0

for g in candidates:
    avg, std = measure(g)
    if baseline is None:
        diff = "—"
        baseline = avg
        base_value = avg
    else:
        diff_ns = avg - base_value
        diff = f"+{diff_ns / 1000:6.1f} µs" if diff_ns > 0 else f"{diff_ns / 1000:7.1f} µs"
    
    print(f"{g} {avg:9,.0f}  {std:8,.0f}  {diff}")