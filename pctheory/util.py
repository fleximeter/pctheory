"""
File: util.py
Author: Jeff Martin
Date: 11/13/2021

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


def factor(n):
    """
    Factors a positive integer
    :param n: An integer
    :returns: A list of factors, in sorted order, including duplicates
    """
    factors = []
    d = 1
    while d <= int(n ** 0.5):
        if n % d == 0:
            factors.append(d)
            n //= d
        else:
            d += 1
        if d == 1:
            d += 1
        # if d > int(n ** 0.5):
        #     factors.append(n)
    factors.append(n)
    # factors.sort()
    return factors


def lcm(integers):
    """
    Computes the LCM of a list of positive integers
    :param integers: A list of positive integers
    :return: The LCM
    """
    factors = {}  # A dictionary of individual factors and their multiplicities
    multiple = 1  # The LCM

    for num in integers:
        cur_factors = factor(num)  # The factors of the current number
        current = 1  # The current factor we are considering
        count = 0  # The number of occurrences of that factor
        for i in range(len(cur_factors)):
            # If we found another occurrence of that factor, increase the count
            if cur_factors[i] == current:
                count += 1
            # Otherwise record the count and move on
            else:
                if current not in factors:
                    factors[current] = count
                elif factors[current] < count:
                    factors[current] = count
                current = cur_factors[i]
                count = 1
            # If we are done, record the count of the last factor
            if i + 1 == len(cur_factors):
                if current not in factors:
                    factors[current] = count
                elif factors[current] < count:
                    factors[current] = count

    # Compute the LCM
    for item in factors:
        multiple *= item ** factors[item]
    # print(multiple)
    return multiple


def map_to_chromatic(scale_map, sequence):
    """
    Maps one sequence of items to another sequence of items. This is useful for doing 
    things like mapping scale degrees 0-6 to actual chromatic pitches. You only need
    to provide a map for one octave, and all transpositions will be accounted for.
    :param scale_map: The scale map
    :param sequence: The sequence to map
    :return: The mapped sequence
    """
    CMOD = 12
    smod = len(scale_map)
    sequence2 = []
    for p in sequence:
        pc = ((p % smod) + smod) % smod
        p2 = (p // smod) * CMOD + scale_map[pc]
        sequence2.append(p2)
    return sequence2


def norgard(n: int):
    """
    Generates the first n numbers of OEIS A004718 (Per Nørgård's infinity series)
    :param n: The number of terms to compute
    :return: The series
    """
    n_list = [0 for i in range(n)]
    i = 0
    m = 0
    while m < n:
        m = 2 * i
        if m < n:
            n_list[m] = -n_list[i]
        m += 1
        if m < n:
            n_list[m] = n_list[i] + 1
        i += 1
    return n_list
