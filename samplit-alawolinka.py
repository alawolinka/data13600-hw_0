import sys
import random

filename = sys.argv[1]

with open(filename, "r") as file:
    for entry in file:
        if random.random() < 0.01:
            print(entry, end="")