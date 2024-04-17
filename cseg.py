"""
File: cseg.py
Author: Jeff Martin
Date: 11/7/2021

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


def com(a: int, b: int):
    """
    The COM function for two cps
    :param a: A cp
    :param b: A cp
    :return: 1 if a < b, 0 if a == b, -1 if a > b
    """
    if a < b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


def com_mx(cseg1: list, cseg2: list):
    """
    Generates a COM matrix for two csegs
    :param cseg1: A cseg
    :param cseg2: A cseg
    :return: The COM matrix
    """
    mx = []
    for i in range(len(cseg2)):
        row = []
        for j in range(len(cseg1)):
            row.append(com(cseg1[j], cseg2[i]))
        mx.append(row)
    return mx


def invert(cseg: list):
    """
    Inverts a cseg
    :param cseg: The cseg
    :return: The inverted cseg
    """
    cseg2 = []
    maxc = max(cseg)
    for cp in cseg:
        cseg2.append(maxc - 1 - cp)
    return cseg2


def retrograde(cseg: list):
    """
    Retrogrades a cseg
    :param cseg: The cseg
    :return: The retrograded cseg
    """
    cseg2 = cseg.copy()
    cseg2.reverse()
    return cseg2


def rotate(cseg: list, n: int):
    """
    Rotates a cseg
    :param cseg: The cseg
    :param n: The index of rotation
    :return: The rotated cseg
    """
    cseg2 = []
    if n < 0:
        n = ((n % len(cseg)) + len(cseg)) % len(cseg)
    for i in range(len(cseg)):
        cseg2.append(cseg[(i - n + len(cseg)) % len(cseg)])
    return cseg2


def simplify(cseg: list):
    """
    Simplifies a cseg
    :param cseg: A cseg
    :return: A simplified form of the cseg
    """
    cseg2 = []
    sort_cseg = list(set(cseg.copy()))
    sort_cseg.sort()
    mapping = {}
    i = 0
    for c in sort_cseg:
        mapping[c] = i
        i += 1
    for c in cseg:
        cseg2.append(mapping[c])
    return cseg2
