import math

x = 0

with open("output.txt", "w") as output:
    for count in range(0, 127):
        x = count * 0.05
        result = math.sin(x)
        print(f"sin({x:.2f}) = {result:+.3f}", file=output)
