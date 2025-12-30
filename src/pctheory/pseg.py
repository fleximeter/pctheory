"""
File: pseg.py
Author: Jeff Martin
Date: 11/1/2021

Copyright © 2021 by Jeffrey Martin. All rights reserved.
Email: jmartin@jeffreymartincomposer.com
Website: https://jeffreymartincomposer.com

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from pctheory.pitch import Pitch, PitchClass


def intervals(pseg: list) -> list:
    """
    Gets the ordered interval content of a pseg
    :param pseg: The pseg
    :return: The ordered interval content as a list
    *Compatible with all Pitch modulos
    """
    intlist = []
    for i in range(1, len(pseg)):
        intlist.append(pseg[i].p - pseg[i - 1].p)
    return intlist
    

def invert(pseg: list) -> list:
    """
    Inverts a pseg
    :param pseg: The pseg
    :return: The inverted pseg
    *Compatible with all Pitch modulos
    """
    pseg2 = []
    if len(pseg) > 0:
        mod = pseg[0].mod
        for p in pseg:
            pseg2.append(Pitch(p.p * -1, mod))
    return pseg2


def make_pseg12(*args) -> list:
    """
    Makes a pseg
    :param args: Ps
    :return: A pseg
    *Compatible only with chromatic psegs
    """
    if len(args) > 0:
        if type(args[0]) == list:
            args = args[0]
        return [Pitch(p, 12) for p in args]
    else:
        return []


def make_pseg24(*args) -> list:
    """
    Makes a pseg
    :param args: Ps
    :return: A pseg
    *Compatible only with microtonal psegs
    """
    if len(args) > 0:
        if type(args[0]) == list:
            args = args[0]
        return [Pitch(p, 24) for p in args]
    else:
        return []


def multiply_order(pseg: list, n: int) -> list:
    """
    Multiplies a pseg's order
    :param pseg: The pseg
    :param n: The multiplier
    :return: The order-multiplied pseg
    *Compatible with all Pitch modulos
    """
    pseg2 = []
    if len(pseg) > 0:
        mod = pseg[0].mod
        for i in range(len(pseg)):
            pseg2.append(Pitch(pseg[(i * n) % len(pseg)].p, mod))
    return pseg2


def retrograde(pseg: list) -> list:
    """
    Retrogrades a pseg
    :param pseg: The pseg
    :return: The retrograded pseg
    *Compatible with all Pitch modulos
    """
    pseg2 = []
    if len(pseg) > 0:
        mod = pseg[0].mod
    for i in range(len(pseg) - 1, -1, -1):
        pseg2.append(Pitch(pseg[i].pc, mod))
    return pseg2


def rotate(pseg: list, n: int) -> list:
    """
    Rotates a pseg
    :param pseg: The pseg
    :param n: The index of rotation
    :return: The rotated pseg
    *Compatible with all Pitch modulos
    """
    pseg2 = []
    if len(pseg) > 0:
        mod = pseg[0].mod
    for i in range(len(pseg)):
        pseg2.append(Pitch(pseg[(i - n) % len(pseg)].p, mod))
    return pseg2


def to_pcseg(pseg: list) -> list:
    """
    Makes a pcseg out of a pseg
    :param pseg: A pseg
    :return: A pcseg
    *Compatible with all Pitch modulos
    """
    if len(pseg) > 0:
        mod = pseg[0].mod
        return [PitchClass(p.pc, mod) for p in pseg]
    else:
        return []


def transpose(pseg: list, n: int) -> list:
    """
    Transposes a pseg
    :param pseg: The pseg
    :param n: The index of transposition
    :return: The transposed pseg
    *Compatible with all Pitch modulos
    """
    pseg2 = []
    if len(pseg) > 0:
        mod = pseg[0].mod
        for p in pseg:
            pseg2.append(Pitch(p.p + n, mod))
    return pseg2
