#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Print with Turtle Graphics using numbers
"""

import turtle
from datetime import datetime
from pathlib import Path
from typing import Generator

from PIL import Image

ROOT_DIR = Path(__file__).parent
DATA_DIR = ROOT_DIR / 'number_data'
OUTPUT_DIR = ROOT_DIR / 'output'
PI_DEC_1K = DATA_DIR / 'pi_dec_1k.txt'
PI_DEC_1M = DATA_DIR / 'pi_dec_1m.txt'

SCALE = 2

if not OUTPUT_DIR.exists():
    OUTPUT_DIR.mkdir()


def save_as_png(canvas, filename=None):

    if filename is None:
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    temp_file = OUTPUT_DIR / f'{filename}.eps'

    canvas.postscript(file = temp_file)

    with Image.open(temp_file) as img:
        img.save(OUTPUT_DIR / f'{filename}.png', 'png')

    temp_file.unlink()


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
        angle = base_n_angle(digit, 3.14)
        t.left(angle)
        t.forward(digit * SCALE)

    save_as_png(turtle.getscreen().getcanvas())
    input()


if __name__ == '__main__':
    main()
