#!/usr/bin/env python3

def print_color_codes():
    for i in range(256):
        print(f"\x1b[38;5;{i}mcolor{i: <5}\x1b[0m", end="")
        if (i + 1) % 8 == 0:
            print()

print_color_codes()
