#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Print with Turtle Graphics using numbers
"""

import math
import turtle
from pathlib import Path
from typing import Generator

ROOT_DIR = Path(__file__).parent
DATA_DIR = ROOT_DIR / 'number_data'
PI_DEC_1K = DATA_DIR / 'pi_dec_1k.txt'
PI_DEC_1M = DATA_DIR / 'pi_dec_1m.txt'

SCALE = 5

def digits(file: Path) -> Generator[int, None, None]:
    for digit in file.read_text(encoding='utf-8'):
        if digit == '.':
            continue
        yield int(digit)

def base_n_angle(num: int, n: int=10):
    full_circle = 360 / n
    return num % n * full_circle

def main():
    t = turtle.Turtle()
    t.speed(0)

    for digit in digits(PI_DEC_1K):
        angle = base_n_angle(digit, 4)
        t.left(angle)
        t.forward(digit * SCALE)
    input()


if __name__ == '__main__':
    main()
